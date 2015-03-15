cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/herwigscripts/qhad2760/dirpthat80_120

cmsRun anaGenJet_HAD_Herwig_cfg.py maxEvents="100000" ptHatLow="80" ptHatHigh="120" &> run_HAD_Herwig2760_80_120.log

rm LHC.tex
rm LHC.log
rm run_HAD_Herwig*
rm Looptools.log

