from numpy import array, rec


class Holder(object):
    pass


var_results = Holder()
var_results.comment = 'VAR test data converted from vars_results.npz'
var_results.causality = array([(9.317172089406967e-08,), (0.5183914225971917,), (4.8960835385969403e-14,)],
      dtype=[('causedby', 'float')])
var_results.name = 'var_results'
var_results.orthirf = array({'realgdp': rec.array([(0.007557357219752236, 0.003948403413668315, 0.02972434157321242),
       (0.0015408726821578582, 0.0010664916255201816, 0.00923575489996933),
       (0.0015874964105555918, 0.0010551760558416706, 0.006102514196485799),
       (0.0007262051539604352, 0.0005562787500837443, 0.003199064883156089),
       (0.0005537000868358786, 0.0003520396722562061, 0.0024372344590635623),
       (0.0003079984190444812, 0.00021674897409108682, 0.0013369479853037147)],
      dtype=[('realgdp', 'float'), ('realcons', 'float'), ('realinv', 'float')]), 'realinv': rec.array([(0.0, 0.0, 0.020741992721114832),
       (0.0006890376065674764, 0.0005338724781743238, 0.004676882806534488),
       (0.00017134455810606506, 0.000682084896451223, -0.0005205835547221123),
       (0.0005217378718553543, 0.00030179909990059973, 0.0026650577026759623),
       (0.00034979575853114173, 0.00022249591743758265, 0.0015804716569096742),
       (0.00017738402507880077, 0.00013384975583249413, 0.0007585745605878197)],
      dtype=[('realgdp', 'float'), ('realcons', 'float'), ('realinv', 'float')]), 'realcons': rec.array([(0.0, 0.005219256972675799, -0.01593559385372415),
       (0.0029937089930834665, 0.000991936965470755, 0.019445506482528015),
       (0.002111631850388755, 0.0013051320985438103, 0.00901674690789421),
       (0.000760821255683657, 0.0006894587307924545, 0.0031531908594739904),
       (0.0006879775935656037, 0.0004452087814044681, 0.0029845646103117077),
       (0.0003908528054047277, 0.00026799713044743445, 0.0017324202804285334)],
      dtype=[('realgdp', 'float'), ('realcons', 'float'), ('realinv', 'float')])}, dtype=object)
var_results.detomega = array([  6.69357627913858242322e-13])
var_results.nirfs = array([ 5.])
var_results.loglike = array([ 1962.57082404432503608405])
var_results.stderr = array([(0.0011190205021849168, 0.0009690469778955306, 0.0058627441569700095),
       (0.169662667084976, 0.14692411307869205, 0.8888923913067142),
       (0.13128502534984174, 0.11368992508162204, 0.6878252130006585),
       (0.02619387125804535, 0.022683312533087908, 0.13723427351570822),
       (0.17352233516355128, 0.15026650017519333, 0.9091138675275061),
       (0.14590394087772843, 0.12634958224138662, 0.7644162686828472),
       (0.02578605367156698, 0.022330151532965133, 0.13509764584216039)],
      dtype=[('realgdp', 'float'), ('realcons', 'float'), ('realinv', 'float')])
var_results.crit = array({'sic': [-27.583016116183746], 'hqic': [-27.789187688321583], 'fpe': [7.421287668356912e-13], 'aic': [-27.92933943967129]}, dtype=object)
var_results.phis = array([[[ 1.                    ,  0.                    ,  0.                    ],
        [ 0.                    ,  1.                    ,  0.                    ],
        [ 0.                    ,  0.                    ,  1.                    ]],

       [[-0.27943473587305184269,  0.67501575174854244743,  0.03321945079394677397],
        [-0.10046797808205484848,  0.26863955252271337626,  0.02573872652220415141],
        [-1.97097367379580989954,  4.41416232699026434005,  0.22547895322388852857]],

       [[-0.04698727419951594098,  0.42980675754266339794,  0.00826075683324488733],
        [-0.17281970983411520937,  0.35046409430422942322,  0.03288425107568751504],
        [ 0.04364931246903419604,  1.65096193457053663778, -0.02509804924346402399]],

       [[-0.11912577490062775665,  0.22257198988626961111,  0.02515370046023775175],
        [-0.07584698388980917749,  0.17652397885529469423,  0.01455014973529403233],
        [-0.60265240582682233494,  0.99644320159959076655,  0.12848609767194643649]],

       [[-0.08883245330826733399,  0.18330532474980901214,  0.01686413466798001443],
        [-0.05728563445875266974,  0.11805267650029765969,  0.01072683422606196188],
        [-0.39750493711843060129,  0.80448318531634888107,  0.07619671254154830597]],

       [[-0.04564844379524263945,  0.10099768165139233478,  0.00855192784337583181],
        [-0.03382143062494445684,  0.07105049775782870669,  0.00645308084098585207],
        [-0.19869441802790854812,  0.44359103295144985957,  0.03657192299636715521]]])
var_results.nahead = array([ 5.])
var_results.totobs = array([ 202.])
var_results.type = array(['const'],
      dtype='|S5')
var_results.obs = array([ 200.])
var_results.irf = array({'realgdp': rec.array([(1.0, 0.0, 0.0), (-0.27943473587305184, -0.10046797808205485, -1.97097367379581),
       (-0.04698727419951594, -0.1728197098341152, 0.043649312469034196),
       (-0.11912577490062776, -0.07584698388980918, -0.6026524058268223),
       (-0.08883245330826733, -0.05728563445875267, -0.3975049371184306),
       (-0.04564844379524264, -0.03382143062494446, -0.19869441802790855)],
      dtype=[('realgdp', 'float'), ('realcons', 'float'), ('realinv', 'float')]), 'realinv': rec.array([(0.0, 0.0, 1.0), (0.033219450793946774, 0.02573872652220415, 0.22547895322388853),
       (0.008260756833244887, 0.032884251075687515, -0.025098049243464024),
       (0.025153700460237752, 0.014550149735294032, 0.12848609767194644),
       (0.016864134667980014, 0.010726834226061962, 0.0761967125415483),
       (0.008551927843375832, 0.006453080840985852, 0.036571922996367155)],
      dtype=[('realgdp', 'float'), ('realcons', 'float'), ('realinv', 'float')]), 'realcons': rec.array([(0.0, 1.0, 0.0), (0.6750157517485424, 0.2686395525227134, 4.414162326990264),
       (0.4298067575426634, 0.3504640943042294, 1.6509619345705366),
       (0.2225719898862696, 0.1765239788552947, 0.9964432015995908),
       (0.183305324749809, 0.11805267650029766, 0.8044831853163489),
       (0.10099768165139233, 0.0710504977578287, 0.44359103295144986)],
      dtype=[('realgdp', 'float'), ('realcons', 'float'), ('realinv', 'float')])}, dtype=object)
var_results.coefs = array([(0.0015269723529158544, 0.005459603048402539, -0.02390252088527764),
       (-0.27943473587305184, -0.10046797808205485, -1.97097367379581),
       (0.6750157517485424, 0.2686395525227134, 4.414162326990264),
       (0.033219450793946774, 0.02573872652220415, 0.22547895322388853),
       (0.008221084912580555, -0.12317392770605443, 0.3807858492371746),
       (0.29045762812920883, 0.23249943591732136, 0.8002809175290293),
       (-0.007320907532428127, 0.023503761040979707, -0.12407906157659883)],
      dtype=[('realgdp', 'float'), ('realcons', 'float'), ('realinv', 'float')])
