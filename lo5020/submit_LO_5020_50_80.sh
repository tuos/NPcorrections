cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/lo5020

cmsRun anaGenJet_LO_cfg.py output="GenJet_LO_R23457_5020_Mar2_Z2pt50to80.root" maxEvents="1000000" processType="NSD" ptHatLow="50" ptHatHigh="80" sqrtS="5020" &> run_LO_5020_50_80.log
