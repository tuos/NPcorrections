cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qhad2760/dirpthat170_220

cmsRun anaGenJet_HAD_Herwig_cfg.py maxEvents="100000" ptHatLow="170" ptHatHigh="220" &> run_HAD_Herwig2760_170_220.log

rm LHC.tex
rm LHC.log
rm run_HAD_Herwig*
rm Looptools.log

