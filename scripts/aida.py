#!/usr/bin/env python

import sys, os
AIDAPYDIR = str(os.environ.get('AIDAPYDIR'))

import argparse
parser = argparse.ArgumentParser(
    description='AIDA histogramming and plotting'
)
parser.add_argument('-g','--generate-histograms',action='store_true',dest='gen_hists',default=False,
                    help='Flag to generate histograms and store in file')
parser.add_argument('-y','--yaml-config',dest='yaml_config',type=str,
                    default=AIDAPYDIR+'/data/template.yaml',
                    help='Path to YAML config')
parser.add_argument('-i','--in-file',dest='in_file',type=str,
                    help='Input ROOT file for the -p and -s options')
parser.add_argument('-p','--generate-plots',dest='gen_plots',nargs='+',type=str,
                    help='Make plots (HARD CODED UNDER CONSTRUCTION)')
parser.add_argument('-r','--root-plots',dest='root_plots',action='store_true',default=False,
                    help='Flag to plot with ROOT instead of matplotlib')
parser.add_argument('-o','--out-file',type=str,dest='out_file',default='aida_histograms.root',
                    help='Name of output file')
parser.add_argument('-s','--split-for-fit',dest='split_for_fit',nargs='+',type=str,
                    help='Run the aidapy.fit.split4fit function with given histogram names')
parser.add_argument('-n','--np-gen',dest='np_gen',action='store_true',
                    help='Flag to generate hists with numpy')

args = parser.parse_args()
if len(sys.argv) < 2:
    parser.print_help()
    exit(0)

import aidapy.hist as aph
import aidapy.plot as app
import aidapy.fit  as apf
import yaml
import ROOT

if args.gen_hists:
    aph.generate_hists(args.yaml_config, output=args.out_file, numpy=args.np_gen)

if args.gen_plots:
    if len(args.gen_plots) == 1 and '.yaml' in args.gen_plots[0]:
        with open(args.gen_plots[0]) as f:
            yaml_top = yaml.load(f)
        for h in yaml_top:
            app.hplot_mpl(ROOT.TFile(args.in_file,'read'),h,
                          xtitle=yaml_top[h]['mpltitles'][0],ytitle=yaml_top[h]['mpltitles'][1])
    else:
        for p in args.gen_plots:
            if args.root_plots:
                app.hplot_root(ROOT.TFile(args.in_file,'read'),p)
            else:
                app.hplot_mpl(ROOT.TFile(args.in_file,'read'),p)

if args.split_for_fit:
    if not args.in_file:
        print('Requires input file!')
        exit()
    apf.split4fit('aida_histograms.root',args.split_for_fit)
