cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/relo7000/dirpthat15_30

cmsRun anaGenJet_LO_Herwig_cfg.py maxEvents="100000" ptHatLow="15" ptHatHigh="30" &> run_LO_Herwig7000_15_30.log

rm LHC.tex
rm LHC.log
rm run_LO_Herwig*
rm Looptools.log

