cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/rehad7000

cmsRun anaGenJet_HAD_cfg.py output="GenJet_HAD_R23457_7000_Mar2_Z2pt50to80.root" maxEvents="1000000" processType="NSD" ptHatLow="50" ptHatHigh="80" sqrtS="7000" &> run_HAD_7000_50_80.log
