import FWCore.ParameterSet.Config as cms

#from PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cff import updatedPatJetCorrFactors
#jetCorrFactors = updatedPatJetCorrFactors.clone(
#    src = cms.InputTag("slimmedJets"),
#    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
#    levels = ['L1FastJet', 'L2Relative', 'L3Absolute'],
#    payload = 'AK4PFchs') 
#
#from  PhysicsTools.PatAlgos.producersLayer1.jetUpdater_cfi import updatedPatJets
#updatedJets = updatedPatJets.clone(
#	addBTagInfo=False,
#	jetSource='slimmedJets',
#	jetCorrFactorsSource=cms.VInputTag(cms.InputTag("jetCorrFactors") ),
#)
bJetVars = cms.EDProducer("JetRegressionVarProducer",
    pvsrc = cms.InputTag("offlineSlimmedPrimaryVertices"),
    #src = cms.InputTag("updatedJets"),
    src = cms.InputTag("slimmedJets"),
    svsrc = cms.InputTag("slimmedSecondaryVertices"),
    gpsrc = cms.InputTag("prunedGenParticles"),
)
updatedJetsWithUserData = cms.EDProducer("PATJetUserDataEmbedder",
        #src = cms.InputTag("updatedJets"),
        src = cms.InputTag("slimmedJets"),
        userFloats = cms.PSet(
            vtxPt = cms.InputTag("bJetVars:vtxPt"),
            vtxMass = cms.InputTag("bJetVars:vtxMass"),
            vtx3dL = cms.InputTag("bJetVars:vtx3dL"),
            vtx3deL = cms.InputTag("bJetVars:vtx3deL"),
            ),
        userInts = cms.PSet(
            vtxNtrk = cms.InputTag("bJetVars:vtxNtrk"),
            ),
        )
jetSecInfoUpdateSequence = cms.Sequence(bJetVars+updatedJetsWithUserData)
#jetSecInfoUpdateSequence = cms.Sequence(jetCorrFactors+updatedJets+bJetVars+updatedJetsWithUserData)
