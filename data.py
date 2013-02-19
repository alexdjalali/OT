voweldset = [
                {   'input': 'ovea',
                    'output': 'o.ve.a',
                    'vvector': {1:0, 2:1, 3:1, 4:0},
                    'optimal': True,
                },

                {
                    'input': 'ovea',
                    'output': 'o.vee',
                    'vvector': {1:0, 2:0, 3:0, 4:1},
                    'optimal': True,
                },

                {
                    'input': 'idea',
                    'output': 'i.de.a',
                    'vvector': {1:0, 2:1, 3:1, 4:0},
                    'optimal': True,
                },

                {
                    'input': 'idea',
                    'output': 'i.dee',
                    'vvector': {1:1, 2:0, 3:0, 4:1},
                    'optimal': False,
                },

                {
                    'input': 'lasi-a',
                    'output': 'la.si.a',
                    'vvector': {1:0, 2:0, 3:1, 4:0},
                    'optimal': True,
                },

                {
                    'input': 'lasi-a',
                    'output': 'la.sii',
                    'vvector': {1:0, 2:0, 3:0, 4:1},
                    'optimal': True,
                },

                {
                    'input': 'rasia',
                    'output': 'ra.si.a',
                    'vvector': {1:0, 2:0, 3:1, 4:0},
                    'optimal': True,
                },

                {
                    'input': 'rasia',
                    'output': 'ra.sii',
                    'vvector': {1:1, 2:0, 3:0, 4:1},
                    'optimal': False,
                },
        ]

# Finnish Case Dataset
casedset = [

                {
                    'input': 'act[trans]',
                    'output': 'GEN',
                    'vvector': {1:0, 2:1, 3:0, 4:1, 5:2, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD1',
                    'vvector': {1:1, 2:1, 3:1, 4:1, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD2',
                    'vvector': {1:0, 2:1, 3:2, 4:2, 5:3, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD3',
                    'vvector': {1:1, 2:1, 3:1, 4:2, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD4',
                    'vvector': {1:0, 2:1, 3:0, 4:1, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD5',
                    'vvector': {1:1, 2:1, 3:1, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD6',
                    'vvector': {1:0, 2:1, 3:2, 4:2, 5:3, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD7',
                    'vvector': {1:1, 2:1, 3:1, 4:2, 5:2, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'GEN',
                    'vvector': {1:0, 2:1, 3:0, 4:0, 5:1, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'act[exist]',
                    'output': 'NOM',
                    'vvector': {1:0, 2:0, 3:1, 4:0, 5:0, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD1',
                    'vvector': {1:0, 2:1, 3:1, 4:1, 5:2, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD2',
                    'vvector': {1:0, 2:0, 3:0, 4:1, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD3',
                    'vvector': {1:0, 2:1, 3:0, 4:0, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD4',
                    'vvector': {1:0, 2:0, 3:1, 4:0, 5:0, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD5',
                    'vvector': {1:0, 2:1, 3:1, 4:1, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD6',
                    'vvector': {1:0, 2:0, 3:0, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'GEN',
                    'vvector': {1:0, 2:2, 3:0, 4:2, 5:2, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'act[pred]',
                    'output': 'NOM',
                    'vvector': {1:0, 2:1, 3:1, 4:1, 5:1, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD1',
                    'vvector': {1:0, 2:2, 3:2, 4:3, 5:3, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD2',
                    'vvector': {1:0, 2:1, 3:1, 4:2, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD3',
                    'vvector': {1:0, 2:2, 3:0, 4:2, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD4',
                    'vvector': {1:0, 2:1, 3:1, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD5',
                    'vvector': {1:0, 2:2, 3:2, 4:3, 5:3, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD6',
                    'vvector': {1:0, 2:1, 3:1, 4:2, 5:2, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'pass[trans]',
                    'output': 'GEN',
                    'vvector': {1:0, 2:1, 3:0, 4:1, 5:2, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'pass[trans]',
                    'output': 'NOM',
                    'vvector': {1:1, 2:1, 3:0, 4:1, 5:1, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'pass[trans]',
                    'output': 'BAD1',
                    'vvector': {1:0, 2:1, 3:0, 4:1, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'pass[trans]',
                    'output': 'BAD2',
                    'vvector': {1:1, 2:1, 3:0, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'pass[exist]',
                    'output': 'GEN',
                    'vvector': {1:0, 2:1, 3:0, 4:0, 5:1, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'pass[exist]',
                    'output': 'NOM',
                    'vvector': {1:0, 2:0, 3:0, 4:0, 5:0, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'pass[exist]',
                    'output': 'BAD1',
                    'vvector': {1:0, 2:1, 3:0, 4:0, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'pass[exist]',
                    'output': 'BAD2',
                    'vvector': {1:0, 2:0, 3:0, 4:0, 5:0, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'pass[pred]',
                    'output': 'GEN',
                    'vvector': {1:0, 2:2, 3:0, 4:2, 5:2, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'pass[pred]',
                    'output': 'NOM',
                    'vvector': {1:0, 2:1, 3:0, 4:1, 5:1, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'pass[pred]',
                    'output': 'BAD1',
                    'vvector': {1:0, 2:2, 3:0, 4:2, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'pass[pred]',
                    'output': 'BAD2',
                    'vvector': {1:0, 2:1, 3:0, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'trans',
                    'output': 'GEN',
                    'vvector': {1:0, 2:0, 3:0, 4:0, 5:1, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'trans',
                    'output': 'BAD1',
                    'vvector': {1:0, 2:0, 3:1, 4:0, 5:0, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'trans',
                    'output': 'BAD2',
                    'vvector': {1:0, 2:0, 3:1, 4:1, 5:2, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'trans',
                    'output': 'BAD3',
                    'vvector': {1:0, 2:0, 3:0, 4:1, 5:1, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'exist',
                    'output': 'NOM',
                    'vvector': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0},
                    'optimal': True,
                },

                {
                    'output': 'exist',
                    'input': 'BAD1',
                    'vvector': {1:0, 2:0, 3:0, 4:0, 5:1, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'pred',
                    'output': 'NOM',
                    'vvector': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'pred',
                    'output': 'BAD1',
                    'vvector': {1:0, 2:0, 3:0, 4:0, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'pred',
                    'output': 'BAD2',
                    'vvector': {1:0, 2:0, 3:0, 4:0, 5:2, 6:2},
                    'optimal': False,
                },
        ]
