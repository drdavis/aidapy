# -*- coding: utf-8 -*-
"""
Help handling ATLAS dataset IDs
"""

import ROOT

_dsid_table = {
    'ttbar_PowPy8'     : [410501] ,
    'ttbar_PowPy8_dil' : [410503] ,
    'ttbar_PowPy6'     : [410000] ,
    'Wt_PowPy6'        : [410015,410016] ,
    'Zjets_S21'        : [i for i in range(361372,361444)] ,
    'Zjets_S22'        : [i for i in range(363361,363411)] + [i for i in range(363102,363123)] ,
    'Zjets_S221'       : [i for i in range(364100,364142)] ,
    'Ztautau_S221'     : [i for i in range(364128,364142)] ,
    'Zll_S221'         : [i for i in range(364100,364128)] ,
    'Wjets_S22'        : [i for i in range(363436,363484)] + [i for i in range(363331,363354)] ,
    'Wjets_S221'       : [i for i in range(364156,364198)] ,
    'Diboson_PowPy8'   : [361601,361603,361607] , #[361610,361604]
    'WW_PowPy8'        : [361600, 361606] ,
    "WW_dedicated"     : [361600, 361078] ,
    "Diboson_dedicated": [361601, 361607, 361603, 361604, 361610] ,
    "RareSM_MG5Py8"    : [410066, 410067, 410068, 410069, 410070, 410073, 410074, 410075]
}

def get_proc_gen(dsid):
    """
    Given a DSID, get the initial state (process) and generator in the
    form [process]_[generator]. The available combinations are listed
    in the get_dsids function documentation.

    Parameters
    ----------
    dsid: int
      self evident

    Returns
    -------
    k: str
      the [process]_[generator] string

    """
    for k, v in _dsid_table.items():
        if dsid in v:
            return k
    return 'Unknown'

def get_dsids(key):
    """
    Get a list of DSIDs associated with a
    process and its generator

    Available process+generator keys:
    ttbar_PowPy8,
    ttbar_PowPy8_dil,
    ttbar_PowPy6,
    Wt_PowPy6,
    Zjets_S21,
    Zjets_S22,
    Zjets_S221,
    Wjets_S22,
    Wjets_S221,
    Diboson_PowPy8,
    WW_PowPy8,
    
    Parameters
    ----------
    key: str
      the string (available listed above)

    Returns
    -------
    list
      List of DSIDs associated with the key
    """
    if key not in _dsid_table:
        raise ValueError(str(key)+' not Available')
    else:
        return _dsid_table[key]

def proc_gen_from_file(rootfile):
    """
    A function to return the initial state (process) and
    generator associated with a ROOT file.

    Parameters
    ----------
    rootfile: str
      Path to ROOT file _or_ the ROOT file itself

    Returns
    -------
    str
      [process]_[generator]

    """
    if isinstance(rootfile, ROOT.TFile):
        pass
    elif isinstance(rootfile, str):
        rootfile = ROOT.TFile(rootfile)
    else:
        raise TypeError('Must be ROOT file or path to ROOT file')
    t = rootfile.Get('AIDA_meta')
    t.GetEntry(0)
    d = int(t.dsid)
    if d == 0:
        return 'Data'
    return get_proc_gen(d)

def sort_files_from_txt(txtfile, procs_and_gens):
    """
    Sort files into a dictionary based on initial state (process) and
    generator.

    Parameters
    ----------
    txtfile: str
      Plain text file listing the full path of all the files to sort
      procs_and_gens : list of [process]_[generator] strings you'd like in
      the final dictionary

    Returns
    -------
    dict
      Dictionary of all processes and the respective files
    """
    retdic = { pandg : [] for pandg in procs_and_gens }
    with open(txtfile) as f:
        for line in f:
            l = line.rstrip()
            p_gen = proc_gen_from_file(l)
            if p_gen in retdic:
                retdic[p_gen].append(l)
    return retdic

_systematic_weights = [
    [ 'weightSyswLum_jvt_UP'                        , 'weightSyswLum_jvt_DOWN'                         , "JVT"               ] ,
    [ 'weightSyswLum_leptonSF_EL_SF_ID_UP'          , 'weightSyswLum_leptonSF_EL_SF_ID_DOWN'           , "Elec SF ID"        ] ,
    [ 'weightSyswLum_leptonSF_EL_SF_Isol_UP'        , 'weightSyswLum_leptonSF_EL_SF_Isol_DOWN'         , "Elec SF Isol"      ] ,
    [ 'weightSyswLum_leptonSF_EL_SF_Reco_UP'        , 'weightSyswLum_leptonSF_EL_SF_Reco_DOWN'         , "Elec SF Reco"      ] ,
    [ 'weightSyswLum_leptonSF_EL_SF_Trigger_UP'     , 'weightSyswLum_leptonSF_EL_SF_Trigger_DOWN'      , "Elec SF Trig"      ] ,
    [ 'weightSyswLum_leptonSF_MU_SF_ID_STAT_UP'     , 'weightSyswLum_leptonSF_MU_SF_ID_STAT_DOWN'      , "Muon SF ID Stat"   ] ,
    [ 'weightSyswLum_leptonSF_MU_SF_ID_SYST_UP'     , 'weightSyswLum_leptonSF_MU_SF_ID_SYST_DOWN'      , "Muon SF ID Syst"   ] ,
    [ 'weightSyswLum_leptonSF_MU_SF_Isol_STAT_UP'   , 'weightSyswLum_leptonSF_MU_SF_Isol_STAT_DOWN'    , "Muon SF Isol Stat" ] ,
    [ 'weightSyswLum_leptonSF_MU_SF_Isol_SYST_UP'   , 'weightSyswLum_leptonSF_MU_SF_Isol_SYST_DOWN'    , "Muon SF Isol Syst" ] ,
    [ 'weightSyswLum_leptonSF_MU_SF_Trigger_STAT_UP', 'weightSyswLum_leptonSF_MU_SF_Trigger_STAT_DOWN' , "Muon SF Trig Stat" ] ,
    [ 'weightSyswLum_leptonSF_MU_SF_Trigger_SYST_UP', 'weightSyswLum_leptonSF_MU_SF_Trigger_SYST_DOWN' , "Muon SF Trig Syst" ] ,
    [ 'weightSyswLum_pileup_UP'                     , 'weightSyswLum_pileup_DOWN'                      , "Pileup"            ] ,
]

_systematic_trees = [
    'EG_RESOLUTION_ALL__1down',
    'EG_RESOLUTION_ALL__1up',
    'EG_SCALE_ALL__1down',
    'EG_SCALE_ALL__1up',
    'JET_21NP_JET_BJES_Response__1down',
    'JET_21NP_JET_BJES_Response__1up',
    'JET_21NP_JET_EffectiveNP_1__1down',
    'JET_21NP_JET_EffectiveNP_1__1up',
    'JET_21NP_JET_EffectiveNP_2__1down',
    'JET_21NP_JET_EffectiveNP_2__1up',
    'JET_21NP_JET_EffectiveNP_3__1down',
    'JET_21NP_JET_EffectiveNP_3__1up',
    'JET_21NP_JET_EffectiveNP_4__1down',
    'JET_21NP_JET_EffectiveNP_4__1up',
    'JET_21NP_JET_EffectiveNP_5__1down',
    'JET_21NP_JET_EffectiveNP_5__1up',
    'JET_21NP_JET_EffectiveNP_6__1down',
    'JET_21NP_JET_EffectiveNP_6__1up',
    'JET_21NP_JET_EffectiveNP_7__1down',
    'JET_21NP_JET_EffectiveNP_7__1up',
    'JET_21NP_JET_EffectiveNP_8restTerm__1down',
    'JET_21NP_JET_EffectiveNP_8restTerm__1up',
    'JET_21NP_JET_EtaIntercalibration_Modelling__1down',
    'JET_21NP_JET_EtaIntercalibration_Modelling__1up',
    'JET_21NP_JET_EtaIntercalibration_NonClosure__1down',
    'JET_21NP_JET_EtaIntercalibration_NonClosure__1up',
    'JET_21NP_JET_EtaIntercalibration_TotalStat__1down',
    'JET_21NP_JET_EtaIntercalibration_TotalStat__1up',
    'JET_21NP_JET_Flavor_Composition__1down',
    'JET_21NP_JET_Flavor_Composition__1up',
    'JET_21NP_JET_Flavor_Response__1down',
    'JET_21NP_JET_Flavor_Response__1up',
    'JET_21NP_JET_Pileup_OffsetMu__1down',
    'JET_21NP_JET_Pileup_OffsetMu__1up',
    'JET_21NP_JET_Pileup_OffsetNPV__1down',
    'JET_21NP_JET_Pileup_OffsetNPV__1up',
    'JET_21NP_JET_Pileup_PtTerm__1down',
    'JET_21NP_JET_Pileup_PtTerm__1up',
    'JET_21NP_JET_Pileup_RhoTopology__1down',
    'JET_21NP_JET_Pileup_RhoTopology__1up',
    'JET_21NP_JET_PunchThrough_MC15__1down',
    'JET_21NP_JET_PunchThrough_MC15__1up',
    'JET_21NP_JET_SingleParticle_HighPt__1down',
    'JET_21NP_JET_SingleParticle_HighPt__1up',
    'JET_JER_SINGLE_NP__1up',
    'MET_SoftTrk_ResoPara',
    'MET_SoftTrk_ResoPerp',
    'MET_SoftTrk_ScaleDown',
    'MET_SoftTrk_ScaleUp',
    'MUON_ID__1down',
    'MUON_ID__1up',
    'MUON_MS__1down',
    'MUON_MS__1up',
    'MUON_SAGITTA_RESBIAS__1down',
    'MUON_SAGITTA_RESBIAS__1up',
    'MUON_SAGITTA_RHO__1down',
    'MUON_SAGITTA_RHO__1up',
    'MUON_SCALE__1down',
    'MUON_SCALE__1up',
]

## tree name, a title
_systematic_ud_prefixes = [ ['EG_RESOLUTION_ALL'                           ,'EG Reso All'             ],
                            ['EG_SCALE_ALL'                                ,'EG Scale All'            ],
                            ['JET_21NP_JET_BJES_Response'                  ,'Jet BJES Response'       ],
                            ['JET_21NP_JET_EffectiveNP_1'                  ,'Jet Eff NP1'             ],
                            ['JET_21NP_JET_EffectiveNP_2'                  ,'Jet Eff NP2'             ],
                            ['JET_21NP_JET_EffectiveNP_3'                  ,'Jet Eff NP3'             ],
                            ['JET_21NP_JET_EffectiveNP_4'                  ,'Jet Eff NP4'             ],
                            ['JET_21NP_JET_EffectiveNP_5'                  ,'Jet Eff NP5'             ],
                            ['JET_21NP_JET_EffectiveNP_6'                  ,'Jet Eff NP6'             ],
                            ['JET_21NP_JET_EffectiveNP_7'                  ,'Jet Eff NP7'             ],
                            ['JET_21NP_JET_EffectiveNP_8restTerm'          ,'Jet Eff 8RT'             ],
                            ['JET_21NP_JET_EtaIntercalibration_Modelling'  ,'Jet EtaInter Modelling'  ],
                            ['JET_21NP_JET_EtaIntercalibration_NonClosure' ,'Jet EtaInter NonClosure' ],
                            ['JET_21NP_JET_EtaIntercalibration_TotalStat'  ,'Jet EtaInter TotalStat'  ],
                            ['JET_21NP_JET_Flavor_Composition'             ,'Jet Flav Compo'          ],
                            ['JET_21NP_JET_Flavor_Response'                ,'Jet Fav Response'        ],
                            ['JET_21NP_JET_Pileup_OffsetMu'                ,'Jet PU OffsetMu'         ],
                            ['JET_21NP_JET_Pileup_OffsetNPV'               ,'Jet PU OffsetNPV'        ],
                            ['JET_21NP_JET_Pileup_PtTerm'                  ,'Jet PU PtTerm'           ],
                            ['JET_21NP_JET_Pileup_RhoTopology'             ,'Jet PU RhoTopo'          ],
                            ['JET_21NP_JET_PunchThrough_MC15'              ,'Jet PunchThrough MC15'   ],
                            ['JET_21NP_JET_SingleParticle_HighPt'          ,'Jet SinglePart HighPt'   ],
                            ['MUON_ID'                                     ,'Muon ID'                 ],
                            ['MUON_MS'                                     ,'Muon MS'                 ],
                            ['MUON_SAGITTA_RESBIAS'                        ,'Muon Sagitta ResBias'    ],
                            ['MUON_SAGITTA_RHO'                            ,'Muon Sagitta Rho'        ],
                            ['MUON_SCALE'                                  ,'Muon Scale'              ],
                            ['MET_SoftTrk_Scale'                           ,'MET SoftTrk Scale'       ]
]

_systematic_singles = [
    ['JET_JER_SINGLE_NP__1up', 'Jet JER Single NP'   ],
    ['MET_SoftTrk_ResoPara',   'MET SoftTrk ResoPara'],
    ['MET_SoftTrk_ResoPerp',   'Met SoftTrk ResoPerp']
]

_systematic_btag_weights = [
    ["weightSyswLum_bTagSF_77_eigenvars_B_up_0",           "weightSyswLum_bTagSF_77_eigenvars_B_down_0",           "b-tag Eigenvars B 0"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_B_up_1",           "weightSyswLum_bTagSF_77_eigenvars_B_down_1",           "b-tag Eigenvars B 1"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_B_up_2",           "weightSyswLum_bTagSF_77_eigenvars_B_down_2",           "b-tag Eigenvars B 2"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_B_up_3",           "weightSyswLum_bTagSF_77_eigenvars_B_down_3",           "b-tag Eigenvars B 3"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_B_up_4",           "weightSyswLum_bTagSF_77_eigenvars_B_down_4",           "b-tag Eigenvars B 4"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_B_up_5",           "weightSyswLum_bTagSF_77_eigenvars_B_down_5",           "b-tag Eigenvars B 5"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_C_up_0",           "weightSyswLum_bTagSF_77_eigenvars_C_down_0",           "b-tag Eigenvars C 0"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_C_up_1",           "weightSyswLum_bTagSF_77_eigenvars_C_down_1",           "b-tag Eigenvars C 1"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_C_up_2",           "weightSyswLum_bTagSF_77_eigenvars_C_down_2",           "b-tag Eigenvars C 2"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_C_up_3",           "weightSyswLum_bTagSF_77_eigenvars_C_down_3",           "b-tag Eigenvars C 3"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_0",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_0",       "b-tag Eigenvars L 0"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_1",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_1",       "b-tag Eigenvars L 1"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_2",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_2",       "b-tag Eigenvars L 2"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_3",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_3",       "b-tag Eigenvars L 3"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_4",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_4",       "b-tag Eigenvars L 4"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_5",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_5",       "b-tag Eigenvars L 5"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_6",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_6",       "b-tag Eigenvars L 6"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_7",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_7",       "b-tag Eigenvars L 7"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_8",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_8",       "b-tag Eigenvars L 8"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_9",       "weightSyswLum_bTagSF_77_eigenvars_Light_down_9",       "b-tag Eigenvars L 9"     ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_10",      "weightSyswLum_bTagSF_77_eigenvars_Light_down_10",      "b-tag Eigenvars L 10"    ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_11",      "weightSyswLum_bTagSF_77_eigenvars_Light_down_11",      "b-tag Eigenvars L 11"    ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_12",      "weightSyswLum_bTagSF_77_eigenvars_Light_down_12",      "b-tag Eigenvars L 12"    ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_13",      "weightSyswLum_bTagSF_77_eigenvars_Light_down_13",      "b-tag Eigenvars L 13"    ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_14",      "weightSyswLum_bTagSF_77_eigenvars_Light_down_14",      "b-tag Eigenvars L 14"    ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_15",      "weightSyswLum_bTagSF_77_eigenvars_Light_down_15",      "b-tag Eigenvars L 15"    ],
    ["weightSyswLum_bTagSF_77_eigenvars_Light_up_16",      "weightSyswLum_bTagSF_77_eigenvars_Light_down_16",      "b-tag Eigenvars L 16"    ],
    ["weightSyswLum_bTagSF_77_extrapolation_from_charm_up","weightSyswLum_bTagSF_77_extrapolation_from_charm_down","b-tag extrap from charm" ],
    ["weightSyswLum_bTagSF_77_extrapolation_up",           "weightSyswLum_bTagSF_77_extrapolation_down",           "b-tag extrap"            ]
]
