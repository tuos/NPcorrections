cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760

cmsRun anaGenJet_HAD_cfg.py output="GenJet_HAD_R23457_2760_Mar2_Z2pt80to120.root" maxEvents="1000000" processType="NSD" ptHatLow="80" ptHatHigh="120" sqrtS="2760" &> run_HAD_2760_80_120.log
