cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src
#cmsenv
eval `scramv1 runtime -sh`

cd /afs/cern.ch/user/t/tuos/work/public/jets/CMSSW_5_3_20/src/NPcorrections/GenJetCrossCheckAnalyzer/test/secondscript/qhad2760

cmsRun anaGenJet_HAD_cfg.py output="GenJet_HAD_R23457_2760_Mar2_Z2pt15to30.root" maxEvents="1000000" processType="NSD" ptHatLow="15" ptHatHigh="30" sqrtS="2760" &> run_HAD_2760_15_30.log
