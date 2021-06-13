import copy
import json
import os
import hashlib
from multiprocessing import Pool


def variants():
    variants = []
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                variants.append({'1': x, '2': y, '3': z})
    return variants


MAX_SCORES = {
    16: 2,
    18: 1,
    22: 1,
    20: 1,
    40: 1,
}
SCORES_ALTERNATIVE = {
    '8th': [16, 22, 40, 18, 20],
    '9th': [16, 22],
    '10th': [16, 40],
    '15th': [16, 18],
    '16th': [18, 20],
    '17th': [16, 22, 40, 18, 20],
}

SCORES_ALTERNATIVE_VARIANT = {
    '8th': [16, 18, 20],
    '9th': [16, 22],
    '10th': [16, 40],
    '15th': [16, 22, 40],
    '16th': [16, 18, 20],
    '17th': [16, 18, 20],
}


RANKS = ['8th', '9th', '10th', '15th', '16th', '17th']


def generate_scores_combo(variant):
    combo_list = [
        {
            'scores': {},
            'max_scores': copy.copy(MAX_SCORES),
        }
    ]
    for rank in RANKS:
        alternatives = SCORES_ALTERNATIVE[rank]
        if variant['2'] == 1:
            alternatives = SCORES_ALTERNATIVE_VARIANT[rank]
        new_combo_list = []
        for combo in combo_list:
            max_scores = combo['max_scores']
            for score in alternatives:
                if max_scores[score] == 0:
                    continue
                if rank == '10th':
                    if score == combo['scores']['9th']:
                        continue
                if variant['2'] == 1:
                    if rank == '15th':
                        if score == combo['scores']['9th'] or score == combo['scores']['10th']:
                            continue
                    elif rank == '16th':
                        if score == combo['scores']['8th']:
                            continue
                    elif rank == '17th':
                        if score == combo['scores']['8th'] or score == combo['scores']['16th']:
                            continue
                else:
                    if rank == '16th':
                        if score == combo['scores']['15th']:
                            continue
                new_combo = copy.deepcopy(combo)
                new_combo['max_scores'][score] -= 1
                new_combo['scores'][rank] = score
                new_combo_list.append(new_combo)
        combo_list = new_combo_list
    return [x['scores'] for x in combo_list]


def run_process(args):
    variant, dictionary, last_letter, scores = args
    print('Starting {}, {}, {}, {}'.format(variant, dictionary, last_letter, scores))
    config = {'variant': variant,
     'dictionary': dictionary,
     'last_letter': last_letter,
     'scores': scores}
    param = json.dumps(config)
    hash = hashlib.md5(param.encode('utf8')).hexdigest()
    os.system('python3 main.py \'{}\' > logs/{}.log 2>&1'.format(param, hash))


if __name__ == '__main__':
    os.system('rm solutions/*.json')
    os.system('rm logs/*.log')
    processes = []
    last_letters = ['d', 'g']
    for variant in variants():
        scores_combo = generate_scores_combo(variant)
        for dictionary in ['sowpods', 'twl']:
            for last_letter in last_letters:
                for scores in scores_combo:
                    processes.append((variant, dictionary, last_letter, scores))
    pool = Pool(processes=8)
    pool.map(run_process, processes)