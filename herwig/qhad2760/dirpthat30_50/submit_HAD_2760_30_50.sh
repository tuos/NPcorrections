cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qhad2760/dirpthat30_50

cmsRun anaGenJet_HAD_Herwig_cfg.py maxEvents="100000" ptHatLow="30" ptHatHigh="50" &> run_HAD_Herwig2760_30_50.log

rm LHC.tex
rm LHC.log
rm run_HAD_Herwig*
rm Looptools.log

