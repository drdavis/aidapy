#!/usr/bin/env python

"""
This file will create a config file for use with the
TRExFitter/TtHFitter package
*** REQUIRES PYTHON3 ***

author: Doug Davis <ddavis@cern.ch>
"""

import sys
import subprocess
import aidapy.meta

f = open('aida.config','w')

print('Job: "myAIDAfit"', file=f)
print('  CmeLabel: "13 TeV"', file=f)
print('  POI: "mu_TTBAR"', file=f)
print('  ReadFrom: HIST', file=f)
print('  HistoPath: "/Users/ddavis/Software/aidapy"', file=f)
print('  Lumi: 1.0', file=f)
print('  LumiLabel: "36.1 fb^{-1}"', file=f)
print('  MCstatThreshold: 0.01', file=f)
print('  ImageFormat: "pdf"', file=f)
print('  SystControlPlots: TRUE', file=f)
print('  DebugLevel: 1', file=f)
print('', file=f)

print('Fit: "fit"', file=f)
print('  FitType: SPLUSB', file=f)
print('  FitRegion: CRSR', file=f)
#print('  FitBlind: TRUE', file=f)
print('  NumCPU: 2', file=f)
print('', file=f)

print('Region: "met_1pj"', file=f)
print('  Type: SIGNAL', file=f)
print('  HistoFile: "aida_histograms_met_1pj"', file=f)
print('  VariableTitle: "#it{E}_{T}^{miss} [GeV]"', file=f)
print('  ShortLabel: "#geq 1 jet"', file=f)
print('  Label: "#geq 1 jet"', file=f)
print('  TexLabel: "$N_{\mathrm{jets}} \geq 1$"', file=f)
#print('  DataType: ASIMOV', file=f)
print('', file=f)

print('Region: "met_0j"', file=f)
print('  Type: SIGNAL', file=f)
print('  HistoFile: "aida_histograms_met_0j"', file=f)
print('  VariableTitle: "#it{E}_{T}^{miss} [GeV]"', file=f)
print('  ShortLabel: "No jets"', file=f)
print('  Label: "No jets"', file=f)
print('  TexLabel: "$N_{\mathrm{jets}} = 0$"', file=f)
#print('  DataType: ASIMOV', file=f)
print('', file=f)

print('Sample: "Data"', file=f)
print('  Title: "Data"', file=f)
print('  Type: DATA', file=f)
print('  HistoName: "Data"', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('Sample: "ttbar"', file=f)
print('  Type: SIGNAL', file=f)
print('  Title: "t#bar{t}"', file=f)
print('  FillColor: 0', file=f)
print('  LineColor: 1', file=f)
print('  HistoName: "ttbar_FULL_main"', file=f)
print('  NormFactor: "mu_TTBAR",1,-10,100', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('Sample: "WtHSGHOST"', file=f)
print('  Type: GHOST', file=f)
print('  Title: "WtHSGHOST"', file=f)
print('  HistoName: "Wt_FULL_sysHS1"', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('Sample: "Wt"', file=f)
print('  Type: SIGNAL', file=f)
print('  Title: "Wt"', file=f)
print('  FillColor: 62', file=f)
print('  LineColor: 1', file=f)
print('  HistoName: "Wt_FULL_main"', file=f)
print('  NormFactor: "mu_WT",1,-10,100', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('Sample: "Ztautau"', file=f)
print('  Type: SIGNAL', file=f)
print('  Title: "Z#rightarrow#tau#tau"', file=f)
print('  FillColor: 32', file=f)
print('  LineColor: 1', file=f)
print('  HistoName: "Ztautau_FULL_main"', file=f)
print('  NormFactor: "mu_ZTAUTAU",1,-10,100', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('Sample: "WW"', file=f)
print('  Type: SIGNAL', file=f)
print('  Title: "WW"', file=f)
print('  FillColor: 42', file=f)
print('  LineColor: 1', file=f)
print('  HistoName: "WW_FULL_main"', file=f)
print('  NormFactor: "mu_WW",1,-10,100', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('Sample: "Diboson"', file=f)
print('  Type: BACKGROUND', file=f)
print('  Title: "Diboson"', file=f)
print('  FillColor: 22', file=f)
print('  LineColor: 1', file=f)
print('  HistoName: "Diboson_FULL_main"', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('Sample: "Fakes"', file=f)
print('  Type: BACKGROUND', file=f)
print('  Title: "Fakes"', file=f)
print('  FillColor: 72', file=f)
print('  LineColor: 1', file=f)
print('  HistoName: "Fakes_FULL_main"', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('Sample: "RareSM"', file=f)
print('  Type: BACKGROUND', file=f)
print('  Title: "RareSM"', file=f)
print('  FillColor: 12', file=f)
print('  LineColor: 1', file=f)
print('  HistoName: "RareSM_FULL_main"', file=f)
print('  Regions: "met_1pj","met_0j"', file=f)
print('', file=f)

print('NormFactor: "mu_TTBAR"', file=f)
print('  Title: "#mu_{t#bar{t}}"', file=f)
print('  Nominal: 1', file=f)
print('  Min: -10', file=f)
print('  Max: 100', file=f)
print('  Samples: ttbar', file=f)
print('', file=f)

print('NormFactor: "mu_WT"', file=f)
print('  Title: "#mu_{Wt}"', file=f)
print('  Nominal: 1', file=f)
print('  Min: -10', file=f)
print('  Max: 100', file=f)
print('  Samples: Wt', file=f)
print('', file=f)

print('NormFactor: "mu_ZTAUTAU"', file=f)
print('  Title: "#mu_{Z#rightarrow#tau#tau}"', file=f)
print('  Nominal: 1', file=f)
print('  Min: -10', file=f)
print('  Max: 100', file=f)
print('  Samples: Ztautau', file=f)
print('', file=f)

print('NormFactor: "mu_WW"', file=f)
print('  Title: "#mu_{WW}"', file=f)
print('  Nominal: 1', file=f)
print('  Min: -10', file=f)
print('  Max: 100', file=f)
print('  Samples: WW', file=f)
print('', file=f)

print('Systematic: "Luminosity"', file=f)
print('  Title: "Luminosity"', file=f)
print('  Type: OVERALL', file=f)
print('  OverallUp:    0.03', file=f)
print('  OverallDown: -0.03', file=f)
print('  Samples: ttbar,Wt,WW,Ztautau,Diboson,Fakes,RareSM', file=f)
print('  Category: Instrumental', file=f)
print('', file=f)

print('Systematic: "ttbar_AR"', file=f)
print('  Title: "ttbar Additional Radiation"', file=f)
print('  Type: HISTO', file=f)
print('  Samples: ttbar', file=f)
print('  HistoNameUp:   "ttbar_FULL_sysARup"', file=f)
print('  HistoNameDown: "ttbar_FULL_sysARdown"', file=f)
print('  Regions: met_1pj,met_0j', file=f)
print('  Symmetrisation: TWOSIDED', file=f)
print('  Category: Theory', file=f)
print('', file=f)

print('Systematic: "ttbar_HS"', file=f)
print('  Title: "ttbar Hard Scatter"', file=f)
print('  Type: HISTO', file=f)
print('  Samples: ttbar', file=f)
print('  HistoNameUp: "ttbar_FULL_sysHS"', file=f)
print('  Symmetrisation: ONESIDED', file=f)
print('  Regions: met_1pj,met_0j', file=f)
print('  Category: Theory', file=f)
print('', file=f)

print('Systematic: "ttbar_FH"', file=f)
print('  Title: "ttbar Factorization/Hadronization"', file=f)
print('  Type: HISTO', file=f)
print('  Samples: ttbar', file=f)
print('  HistoNameUp: "ttbar_FULL_sysFH"', file=f)
print('  Symmetrisation: ONESIDED', file=f)
print('  Regions: met_1pj,met_0j', file=f)
print('  Category: Theory', file=f)
print('', file=f)

print('Systematic: "Wt_AR"', file=f)
print('  Title: "Wt Additional Radiation"', file=f)
print('  Type: HISTO', file=f)
print('  Samples: Wt', file=f)
print('  HistoNameUp:   "Wt_FULL_sysARup"', file=f)
print('  HistoNameDown: "Wt_FULL_sysARdown"', file=f)
print('  Regions: met_1pj,met_0j', file=f)
print('  Symmetrisation: TWOSIDED', file=f)
print('  Category: Theory', file=f)
print('', file=f)

print('Systematic: "Wt_DR_DS"', file=f)
print('  Title: "Wt DR vs DS"', file=f)
print('  Type: HISTO', file=f)
print('  Samples: Wt', file=f)
print('  HistoNameUp: "Wt_FULL_sysDS"', file=f)
print('  Symmetrisation: ONESIDED', file=f)
print('  Regions: met_1pj,met_0j', file=f)
print('  Category: Theory', file=f)
print('', file=f)

print('Systematic: "Wt_FH"', file=f)
print('  Title: "Wt Factorization/Hadronization"', file=f)
print('  Type: HISTO', file=f)
print('  Samples: Wt', file=f)
print('  HistoNameUp: "Wt_FULL_sysFH"', file=f)
print('  Symmetrisation: ONESIDED', file=f)
print('  Regions: met_1pj,met_0j', file=f)
print('  Category: Theory', file=f)
print('', file=f)

print('Systematic: "Wt_HS"', file=f)
print('  Title: "Wt Hard Scatter"', file=f)
print('  Type: HISTO', file=f)
print('  Samples: Wt', file=f)
print('  HistoNameUp: "Wt_FULL_sysHS2"', file=f)
#print('  HistoNameDown: "Wt_FULL_sysHS1"', file=f)
print('  ReferenceSample: WtHSGHOST', file=f)
print('  Symmetrisation: ONESIDED', file=f)
print('  Regions: met_1pj,met_0j', file=f)
print('  Category: Theory', file=f)
print('', file=f)

for s in aidapy.meta._systematic_ud_prefixes:
    up = '__1up"'
    down = '__1down"'
    if 'MET_' in s:
        up = 'Up"'
        down = 'Down"'
    print('Systematic: "'+s+'"', file=f)
    print('  Title: "'+s+'"', file=f)
    print('  Samples: ttbar,Wt,WW,Ztautau,Diboson,Fakes,RareSM', file=f)
    print('  Type: HISTO', file=f)
    print('  HistoNameSufUp: "_'+s+up, file=f)
    print('  HistoNameSufDown: "_'+s+down, file=f)
    print('  Regions: met_1pj,met_0j', file=f)
    print('  Symmetrisation: TWOSIDED', file=f)
    print('  Category: Instrumental', file=f)
    print('', file=f)

for s in aidapy.meta._systematic_singles:
    print('Systematic: "'+s+'"', file=f)
    print('  Title: "'+s+'"', file=f)
    print('  Samples: ttbar,Wt,WW,Ztautau,Diboson,Fakes,RareSM', file=f)
    print('  Regions: met_1pj,met_0j', file=f)
    print('  Type: HISTO', file=f)
    print('  HistoNameSufUp: "_'+s+'"', file=f)
    print('  Symmetrisation: ONESIDED', file=f)
    print('  Category: Instrumental', file=f)
    print('', file=f)

for s in aidapy.meta._systematic_weights:
    up, down = s[0], s[1]
    name = up.split('_UP')[0].split('weightSyswLum_')[-1]
    print('Systematic: "'+name+'"', file=f)
    print('  Title: "'+name+'"', file=f)
    print('  Samples: ttbar,Wt,WW,Ztautau,Diboson,Fakes,RareSM', file=f)
    print('  Regions: met_1pj,met_0j', file=f)
    print('  Type: HISTO', file=f)
    print('  Symmetrisation: TWOSIDED', file=f)
    print('  HistoNameSufUp: "_'+up+'"', file=f)
    print('  HistoNameSufDown: "_'+down+'"', file=f)
    print('', file=f)

f.close()

if 'andrun' in sys.argv:
    subprocess.call('rm -rf myAIDAfit', shell=True)
    print('myFit.exe h aida.config')
    print('myFit.exe w aida.config')
    print('myFit.exe f aida.config')
    print('myFit.exe d aida.config')
    print('myFit.exe p aida.config')
