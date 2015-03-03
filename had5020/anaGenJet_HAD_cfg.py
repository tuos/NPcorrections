import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import os

process = cms.Process('GEN')

# ================= var parsing ======================

options = VarParsing.VarParsing ('standard')

options.output = 'genJetSpectrum_HAD.root'
options.maxEvents = 100

options.register('processType',
                 "NSD",
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 "Pythia process type with pT_hat range")

options.register('sqrtS',
                 2760.0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.float,
                 "Center-of-mass energy")

options.register('ptHatLow',
                 120,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Minimum pt-hat")

options.register('ptHatHigh',
                 160,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 "Maximum pt-hat")

options.parseArguments()

# ================= load fragments =====================

process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')
process.load('Configuration/StandardSequences/EndOfProcess_cff')
process.load('Configuration/EventContent/EventContent_cff')
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("RecoJets.Configuration.GenJetParticles_cff")
process.load("RecoJets.Configuration.RecoGenJets_cff")
#process.load("../python/genjetcrosscheckanalyzer_cfi")

# ================ options and files ====================

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)
process.options = cms.untracked.PSet(
    Rethrow = cms.untracked.vstring('ProductNotFound'),
    makeTriggerResults = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(True)
)

process.source = cms.Source("EmptySource")

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.output)
)

from IOMC.RandomEngine.RandomServiceHelper import RandomNumberServiceHelper
randSvc = RandomNumberServiceHelper(process.RandomNumberGeneratorService)
randSvc.populate()

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# ============= Pythia setting  ================================
from Configuration.Generator.PythiaUEZ2Settings_cfi import *
#from Configuration.Generator.PythiaUEZ2starSettings_cfi import *
#from PythiaUEAMBT2Settings_cfi import *

process.generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    PNInitialState = cms.untracked.bool(True),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(2760.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
         pythiaUESettings = cms.vstring(
            'MSTU(21)=1     ! Check on possible errors during program execution', 
            'MSTJ(22)=2     ! Decay those unstable particles', 
            'PARJ(71)=10 .  ! for which ctau  10 mm', 
            'MSTP(33)=0     ! no K factors in hard cross sections', 
            'MSTP(2)=1      ! which order running alphaS', 
            'MSTP(51)=10042 ! structure function chosen (external PDF CTEQ6L1)', 
            'MSTP(52)=2     ! work with LHAPDF', 
            'PARP(82)=1.832 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1800. ! sqrts for which PARP82 is set', 
            'PARP(90)=0.275 ! Multiple interactions: rescaling power', 
            'MSTP(95)=6     ! CR (color reconnection parameters)', 
            'PARP(77)=1.016 ! CR', 
            'PARP(78)=0.538 ! CR', 
            'PARP(80)=0.1   ! Prob. colored parton from BBR', 
            'PARP(83)=0.356 ! Multiple interactions: matter distribution parameter', 
            'PARP(84)=0.651 ! Multiple interactions: matter distribution parameter', 
            'PARP(62)=1.025 ! ISR cutoff', 
            'MSTP(91)=1     ! Gaussian primordial kT', 
            'PARP(93)=10.0  ! primordial kT-max', 
            'MSTP(81)=21    ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4     ! Defines the multi-parton model',
            'MSTP(111)=1', #hadronisation off =0
            ),
         #have to change these parameters to match the ones for HAD,MPI etc... 
         processParameters = cms.vstring(
                 'MSEL=1         ! High Pt QCD',
                 #'CKIN(3)=15  ! minimum pt hat for hard interactions',
                 ),
         parameterSets = cms.vstring('pythiaUESettings',
                                     'processParameters',
                                     #'pthatLow',
                                     #'pthatHigh')
                                    )
         )
)

process.gen_step = cms.Path(process.generator
                            * process.genParticles )

# update the process parameters and c.o.m energy
from customiseGEN2_cfi import *

updatePy6ProcParameters(process.generator,options.processType,options.ptHatLow,options.ptHatHigh,options.sqrtS)

print process.generator.PythiaParameters.processParameters

# ============= Gen jet ================================
process.ak2GenJets = process.ak5GenJets.clone( rParam = 0.2 )
process.ak3GenJets = process.ak5GenJets.clone( rParam = 0.3 )
process.ak4GenJets = process.ak5GenJets.clone( rParam = 0.4 )
process.ak7GenJets = process.ak5GenJets.clone( rParam = 0.7 )

process.genjet_step = cms.Path(process.genJetParticles 
                               * process.ak2GenJets
                               * process.ak3GenJets
                               * process.ak4GenJets
                               * process.ak5GenJets
                               * process.ak7GenJets
)

# =============== Analysis =============================
process.ak3GenJetSpectrum = cms.EDAnalyzer('GenJetCrossCheckAnalyzer',
    genJetSrc = cms.InputTag("ak3GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    doCMatrix = cms.bool(True),
    doFlavor = cms.bool(False),
    flavorSrc = cms.InputTag("flavourByRef"),
    flavorId = cms.vint32(0),    
    jetsByAbsRapidity = cms.bool(False),
    etaMin = cms.double(-1.0),
    etaMax = cms.double(1.0),
    jetRadius = cms.double(0.3),
    pthatMin = cms.double(options.ptHatLow),
    pthatMax = cms.double(options.ptHatHigh),
    ptBins = cms.vdouble( 3, 4, 5, 7, 9, 12, 15, 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,1000 ),
    pythiaProcess = cms.string(options.processType ),
    dijetEtaBins = cms.vdouble( -3.01, -2.63333, -2.07, -1.78833, -1.50667, -1.225, -0.943333, -0.661667, -0.38, -0.0983333, 0.183333, 0.465, 0.746667, 1.02833, 1.31, 1.59167, 1.87333, 2.43667, 3.0),
    dijetEtaWeights = cms.vdouble( 1, 0.772085, 0.701301, 0.753585, 0.813741, 0.882849, 0.943137, 0.977332, 0.993655, 1.0375, 1.04713, 1.04826, 1.05517, 1.05983, 1.0723, 1.06945, 1.01587, 1.41731 )    
)

#R=0.3 
process.ak3GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum.clone(
    doCMatrix = cms.bool(False)
)
process.ak3GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.0),
    etaMax = cms.double(2.0)
)
process.ak3GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.5),
    etaMax = cms.double(-2.0)
)
process.ak3GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-2.0),
    etaMax = cms.double(-1.5)
)
process.ak3GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-1.5),
    etaMax = cms.double(-1.0)
)
process.ak3GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-1.0),
    etaMax = cms.double(-0.5)
)
process.ak3GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(-0.5),
    etaMax = cms.double(0.5)
)
process.ak3GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(0.5),
    etaMax = cms.double(1.0)
)
process.ak3GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(1.0),
    etaMax = cms.double(1.5)
)
process.ak3GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_n10_p10.clone(
    etaMin = cms.double(1.5),
    etaMax = cms.double(2.0)
)

#R=0.2
process.ak2GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)
process.ak2GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak2GenJets")
)

#R=0.4
process.ak4GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)

#R=0.5
process.ak5GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)
process.ak5GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak5GenJets")
)

#R=0.7
process.ak7GenJetSpectrum_n10_p10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n20_p20 = process.ak3GenJetSpectrum_n20_p20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n25_n20 = process.ak3GenJetSpectrum_n25_n20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n20_n15 = process.ak3GenJetSpectrum_n20_n15.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n15_n10 = process.ak3GenJetSpectrum_n15_n10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n10_n05 = process.ak3GenJetSpectrum_n10_n05.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_n05_p05 = process.ak3GenJetSpectrum_n05_p05.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p05_p10 = process.ak3GenJetSpectrum_p05_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p10_p15 = process.ak3GenJetSpectrum_p10_p15.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_p15_p20 = process.ak3GenJetSpectrum_p15_p20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)

process.ak5GenJetSpectrum_QCD10001_00_05 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(0.0),
    etaMax = cms.double(0.5),
    jetRadius = cms.double(0.5),
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,846,1684)
)

process.ak5GenJetSpectrum_QCD10001_05_10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(0.5),
    etaMax = cms.double(1.0),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,790,1684)
)

process.ak5GenJetSpectrum_QCD10001_10_15 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(1.0),
    etaMax = cms.double(1.5),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,1410 )
)

process.ak5GenJetSpectrum_QCD10001_15_20 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(1.5),
    etaMax = cms.double(2.0),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,1032 )
)

process.ak5GenJetSpectrum_QCD10001_20_25 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(2.0),
    etaMax = cms.double(2.5),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,330,362,395,430,737 )
)

process.ak5GenJetSpectrum_QCD10001_25_30 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak5GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(2.5),
    etaMax = cms.double(3.0),
    jetRadius = cms.double(0.5),    
    ptBins = cms.vdouble( 18,21,24,28,32,37,43,49,56,64,74,84,97,114,133,153,174,196,220,245,272,300,468 )
)


process.ak3GenJetSpectrum_QCD10001_00_05 = process.ak5GenJetSpectrum_QCD10001_00_05.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_05_10 = process.ak5GenJetSpectrum_QCD10001_05_10.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_10_15 = process.ak5GenJetSpectrum_QCD10001_10_15.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_15_20 = process.ak5GenJetSpectrum_QCD10001_15_20.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_20_25 = process.ak5GenJetSpectrum_QCD10001_20_25.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD10001_25_30 = process.ak5GenJetSpectrum_QCD10001_25_30.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)


process.ak4GenJetSpectrum_QCD10001_00_05 = process.ak5GenJetSpectrum_QCD10001_00_05.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_05_10 = process.ak5GenJetSpectrum_QCD10001_05_10.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_10_15 = process.ak5GenJetSpectrum_QCD10001_10_15.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_15_20 = process.ak5GenJetSpectrum_QCD10001_15_20.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_20_25 = process.ak5GenJetSpectrum_QCD10001_20_25.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)
process.ak4GenJetSpectrum_QCD10001_25_30 = process.ak5GenJetSpectrum_QCD10001_25_30.clone(
    genJetSrc = cms.InputTag("ak4GenJets")
)

process.ak7GenJetSpectrum_QCD10001_00_05 = process.ak5GenJetSpectrum_QCD10001_00_05.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_05_10 = process.ak5GenJetSpectrum_QCD10001_05_10.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_10_15 = process.ak5GenJetSpectrum_QCD10001_10_15.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_15_20 = process.ak5GenJetSpectrum_QCD10001_15_20.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_20_25 = process.ak5GenJetSpectrum_QCD10001_20_25.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)
process.ak7GenJetSpectrum_QCD10001_25_30 = process.ak5GenJetSpectrum_QCD10001_25_30.clone(
    genJetSrc = cms.InputTag("ak7GenJets")
)


process.ak7GenJetSpectrum_QCD11004_00_05 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(0.0),
    etaMax = cms.double(0.5),
    jetRadius = cms.double(0.7),
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,790,846,905,967,1032,1101,1172,1248,1327,1410,1497,1588,1784,2116 )
)

process.ak7GenJetSpectrum_QCD11004_05_10 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(0.5),
    etaMax = cms.double(1.0),
    jetRadius = cms.double(0.7),
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,790,846,905,967,1032,1101,1172,1248,1327,1410,1784 )
)

process.ak7GenJetSpectrum_QCD11004_10_15 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(1.0),
    etaMax = cms.double(1.5),
    jetRadius = cms.double(0.7),    
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,790,846,905,967,1032,1101,1172,1684 )
)

process.ak7GenJetSpectrum_QCD11004_15_20 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(1.5),
    etaMax = cms.double(2.0),
    jetRadius = cms.double(0.7),    
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,737,790,846,905,967,1248  )
)

process.ak7GenJetSpectrum_QCD11004_20_25 = process.ak3GenJetSpectrum_n10_p10.clone(
    genJetSrc = cms.InputTag("ak7GenJets"),
    genParticleSrc = cms.InputTag("genParticles"),
    jetsByAbsRapidity = cms.bool(True),
    etaMin = cms.double(2.0),
    etaMax = cms.double(2.5),
    jetRadius = cms.double(0.7),
    ptBins = cms.vdouble( 114,133,153,174,196,220,245,272,300,330,362,395,430,468,507,548,592,638,686,905  )
)

process.ak3GenJetSpectrum_QCD11004_00_05 = process.ak7GenJetSpectrum_QCD11004_00_05.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD11004_05_10 = process.ak7GenJetSpectrum_QCD11004_05_10.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD11004_10_15 = process.ak7GenJetSpectrum_QCD11004_10_15.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD11004_15_20 = process.ak7GenJetSpectrum_QCD11004_15_20.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)
process.ak3GenJetSpectrum_QCD11004_20_25 = process.ak7GenJetSpectrum_QCD11004_20_25.clone(
    genJetSrc = cms.InputTag("ak3GenJets")
)

process.ana_step = cms.Path(
#    process.ak3GenJetSpectrum
    process.ak3GenJetSpectrum_n10_p10 * 
    process.ak3GenJetSpectrum_n20_p20 *
    process.ak3GenJetSpectrum_n25_n20 *
    process.ak3GenJetSpectrum_n20_n15 *
    process.ak3GenJetSpectrum_n15_n10 *
    process.ak3GenJetSpectrum_n10_n05 *
    process.ak3GenJetSpectrum_n05_p05 *
    process.ak3GenJetSpectrum_p05_p10 *
    process.ak3GenJetSpectrum_p10_p15 *
    process.ak3GenJetSpectrum_p15_p20 *

    process.ak2GenJetSpectrum_n10_p10 * 
    process.ak2GenJetSpectrum_n20_p20 *
    process.ak2GenJetSpectrum_n25_n20 *
    process.ak2GenJetSpectrum_n20_n15 *
    process.ak2GenJetSpectrum_n15_n10 *
    process.ak2GenJetSpectrum_n10_n05 *
    process.ak2GenJetSpectrum_n05_p05 *
    process.ak2GenJetSpectrum_p05_p10 *
    process.ak2GenJetSpectrum_p10_p15 *
    process.ak2GenJetSpectrum_p15_p20 *

    process.ak4GenJetSpectrum_n10_p10 * 
    process.ak4GenJetSpectrum_n20_p20 *
    process.ak4GenJetSpectrum_n25_n20 *
    process.ak4GenJetSpectrum_n20_n15 *
    process.ak4GenJetSpectrum_n15_n10 *
    process.ak4GenJetSpectrum_n10_n05 *
    process.ak4GenJetSpectrum_n05_p05 *
    process.ak4GenJetSpectrum_p05_p10 *
    process.ak4GenJetSpectrum_p10_p15 *
    process.ak4GenJetSpectrum_p15_p20 *

    process.ak5GenJetSpectrum_n10_p10 * 
    process.ak5GenJetSpectrum_n20_p20 *
    process.ak5GenJetSpectrum_n25_n20 *
    process.ak5GenJetSpectrum_n20_n15 *
    process.ak5GenJetSpectrum_n15_n10 *
    process.ak5GenJetSpectrum_n10_n05 *
    process.ak5GenJetSpectrum_n05_p05 *
    process.ak5GenJetSpectrum_p05_p10 *
    process.ak5GenJetSpectrum_p10_p15 *
    process.ak5GenJetSpectrum_p15_p20 *

    process.ak7GenJetSpectrum_n10_p10 * 
    process.ak7GenJetSpectrum_n20_p20 *
    process.ak7GenJetSpectrum_n25_n20 *
    process.ak7GenJetSpectrum_n20_n15 *
    process.ak7GenJetSpectrum_n15_n10 *
    process.ak7GenJetSpectrum_n10_n05 *
    process.ak7GenJetSpectrum_n05_p05 *
    process.ak7GenJetSpectrum_p05_p10 *
    process.ak7GenJetSpectrum_p10_p15 *
    process.ak7GenJetSpectrum_p15_p20 

#    process.ak5GenJetSpectrum_QCD10001_00_05 *
#    process.ak5GenJetSpectrum_QCD10001_05_10 *
#    process.ak5GenJetSpectrum_QCD10001_10_15 *
#    process.ak5GenJetSpectrum_QCD10001_15_20 *
#    process.ak5GenJetSpectrum_QCD10001_20_25 *
#    process.ak5GenJetSpectrum_QCD10001_25_30 *
#    process.ak3GenJetSpectrum_QCD10001_00_05 *
#    process.ak3GenJetSpectrum_QCD10001_05_10 *
#    process.ak3GenJetSpectrum_QCD10001_10_15 *
#    process.ak3GenJetSpectrum_QCD10001_15_20 *
#    process.ak3GenJetSpectrum_QCD10001_20_25 *
#    process.ak3GenJetSpectrum_QCD10001_25_30 *
#    process.ak4GenJetSpectrum_QCD10001_00_05 *
#    process.ak4GenJetSpectrum_QCD10001_05_10 *
#    process.ak4GenJetSpectrum_QCD10001_10_15 *
#    process.ak4GenJetSpectrum_QCD10001_15_20 *
#    process.ak4GenJetSpectrum_QCD10001_20_25 *
#    process.ak4GenJetSpectrum_QCD10001_25_30 *
#    process.ak7GenJetSpectrum_QCD10001_00_05 *
#    process.ak7GenJetSpectrum_QCD10001_05_10 *
#    process.ak7GenJetSpectrum_QCD10001_10_15 *
#    process.ak7GenJetSpectrum_QCD10001_15_20 *
#    process.ak7GenJetSpectrum_QCD10001_20_25 *
#    process.ak7GenJetSpectrum_QCD10001_25_30 *
#    process.ak7GenJetSpectrum_QCD11004_00_05 *
#    process.ak7GenJetSpectrum_QCD11004_05_10 *
#    process.ak7GenJetSpectrum_QCD11004_10_15 *
#    process.ak7GenJetSpectrum_QCD11004_15_20 *
#    process.ak7GenJetSpectrum_QCD11004_20_25 *
#    process.ak3GenJetSpectrum_QCD11004_00_05 *
#    process.ak3GenJetSpectrum_QCD11004_05_10 *
#    process.ak3GenJetSpectrum_QCD11004_10_15 *
#    process.ak3GenJetSpectrum_QCD11004_15_20 *
#    process.ak3GenJetSpectrum_QCD11004_20_25 
)

process.schedule = cms.Schedule(process.gen_step,
                                process.genjet_step,
                                process.ana_step)


