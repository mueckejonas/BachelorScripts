import ROOT
import numpy as np

print("starting the program")

#task is to take Root Files as input and save them as numpy arrays

#loads data from ROOT and saves them as numpy arrays
def loadRootDataJet1(fileName,treeName,eventNum,outDirectory):
    inFile = ROOT.TFile.Open(fileName,"READ")
    tree = inFile.Get(treeName)

    pt = np.empty(eventNum) #transverse momentum
    y = np.empty(eventNum) #rapidity
    eta = np.empty(eventNum) #polar angle = y
    m = np.empty(eventNum) #mass
    phi = np.empty(eventNum) #azimuthal angle
    jec = np.empty(eventNum) #jet energy correction
    muf  = np.empty(eventNum)#muon energy fraction
    nhf  = np.empty(eventNum)#neutral energy fraction
    chf  = np.empty(eventNum)#charged energy fraction
    area  = np.empty(eventNum)#jet catchment area, for JECs
    nemf  = np.empty(eventNum)#neutral electromagnetic energy fraction
    cemf = np.empty(eventNum) #charged electromagnetic energy fraction
    btagDeepFlavB  = np.empty(eventNum)#DeepJet b+bb+lepb tag discriminator
    nConstituents  = np.empty(eventNum)#number of particles in the jet



    counter = 0

    for entry in tree:
        pt[counter] = entry.jetAK4_pt1
        y[counter] = entry.jetAK4_y1
        eta[counter] = entry.jetAK4_eta1
        m[counter] = entry.jetAK4_mass1
        jec[counter] = entry.jetAK4_jec1
        phi[counter] = entry.jetAK4_phi1
        muf[counter] = entry.jetAK4_muf1
        nhf[counter] = entry.jetAK4_nhf1
        chf[counter] = entry.jetAK4_chf1
        area[counter] = entry.jetAK4_area1
        nemf[counter] = entry.jetAK4_nemf1
        cemf[counter] = entry.jetAK4_cemf1
        btagDeepFlavB[counter] = entry.jetAK4_btagDeepFlavB1
        nConstituents[counter] = entry.jetAK4_nConstituents1

        counter += 1
        if counter == eventNum:
            break

    np.save(outDirectory+"pt1_values.npy",pt)
    np.save(outDirectory+"y1_values.npy",y)
    np.save(outDirectory+"eta1_values.npy",eta)
    np.save(outDirectory+"m1_values.npy",m)
    np.save(outDirectory+"phi1_values.npy",phi)
    np.save(outDirectory+"jec1_values.npy",jec)
    np.save(outDirectory+"muf1_values.npy",muf)
    np.save(outDirectory+"nhf1_values.npy",nhf)
    np.save(outDirectory+"chf1_values.npy",chf)
    np.save(outDirectory+"area1_values.npy",area)
    np.save(outDirectory+"nemf1_values.npy",nemf)
    np.save(outDirectory+"cemf1_values.npy",cemf)
    np.save(outDirectory+"btagDeepFlavB1_values.npy",btagDeepFlavB)
    np.save(outDirectory+"nConstituents1_values.npy",nConstituents)
    print("Jet 1 numpy arrays saved")
    return pt,eta,phi,m,y

def loadRootDataJet2(fileName,treeName,eventNum,outDirectory):
    inFile = ROOT.TFile.Open(fileName,"READ")
    tree = inFile.Get(treeName)

    pt = np.empty(eventNum) #transverse momentum
    y = np.empty(eventNum) #rapidity
    eta = np.empty(eventNum) #polar angle = y
    m = np.empty(eventNum) #mass
    phi = np.empty(eventNum) #azimuthal angle
    jec = np.empty(eventNum) #jet energy correction
    muf  = np.empty(eventNum)#muon energy fraction
    nhf  = np.empty(eventNum)#neutral energy fraction
    chf  = np.empty(eventNum)#charged energy fraction
    area  = np.empty(eventNum)#jet catchment area, for JECs
    nemf  = np.empty(eventNum)#neutral electromagnetic energy fraction
    cemf = np.empty(eventNum) #charged electromagnetic energy fraction
    btagDeepFlavB  = np.empty(eventNum)#DeepJet b+bb+lepb tag discriminator
    nConstituents  = np.empty(eventNum)#number of particles in the jet



    counter = 0

    for entry in tree:
        pt[counter] = entry.jetAK4_pt2
        y[counter] = entry.jetAK4_y2
        eta[counter] = entry.jetAK4_eta2
        m[counter] = entry.jetAK4_mass2
        jec[counter] = entry.jetAK4_jec2
        phi[counter] = entry.jetAK4_phi2
        muf[counter] = entry.jetAK4_muf2
        nhf[counter] = entry.jetAK4_nhf2
        chf[counter] = entry.jetAK4_chf2
        area[counter] = entry.jetAK4_area2
        nemf[counter] = entry.jetAK4_nemf2
        cemf[counter] = entry.jetAK4_cemf2
        btagDeepFlavB[counter] = entry.jetAK4_btagDeepFlavB2
        nConstituents[counter] = entry.jetAK4_nConstituents2

        counter += 1
        if counter == eventNum:
            break

    np.save(outDirectory+"pt2_values.npy",pt)
    np.save(outDirectory+"y2_values.npy",y)
    np.save(outDirectory+"eta2_values.npy",eta)
    np.save(outDirectory+"m2_values.npy",m)
    np.save(outDirectory+"jec2_values.npy",jec)
    np.save(outDirectory+"muf2_values.npy",muf)
    np.save(outDirectory+"phi2_values.npy",phi)
    np.save(outDirectory+"nhf2_values.npy",nhf)
    np.save(outDirectory+"chf2_values.npy",chf)
    np.save(outDirectory+"area2_values.npy",area)
    np.save(outDirectory+"nemf2_values.npy",nemf)
    np.save(outDirectory+"cemf2_values.npy",cemf)
    np.save(outDirectory+"btagDeepFlavB2_values.npy",btagDeepFlavB)
    np.save(outDirectory+"nConstituents2_values.npy",nConstituents)
    print("Jet 2 numpy arrays saved")
    return pt,eta,phi,m,y

def loadRootDataJet3(fileName,treeName,eventNum,outDirectory):
    inFile = ROOT.TFile.Open(fileName,"READ")
    tree = inFile.Get(treeName)

    pt = np.empty(eventNum) #transverse momentum
    y = np.empty(eventNum) #rapidity
    eta = np.empty(eventNum) #polar angle = y
    m = np.empty(eventNum) #mass
    phi = np.empty(eventNum) #azimuthal angle
    jec = np.empty(eventNum) #jet energy correction
    muf  = np.empty(eventNum)#muon energy fraction
    nhf  = np.empty(eventNum)#neutral energy fraction
    chf  = np.empty(eventNum)#charged energy fraction
    area  = np.empty(eventNum)#jet catchment area, for JECs
    nemf  = np.empty(eventNum)#neutral electromagnetic energy fraction
    cemf = np.empty(eventNum) #charged electromagnetic energy fraction
    btagDeepFlavB  = np.empty(eventNum)#DeepJet b+bb+lepb tag discriminator
    nConstituents  = np.empty(eventNum)#number of particles in the jet




    counter = 0

    for entry in tree:

        pt[counter] = entry.jetAK4_pt3
        y[counter] = entry.jetAK4_y3
        eta[counter] = entry.jetAK4_eta3
        m[counter] = entry.jetAK4_mass3
        jec[counter] = entry.jetAK4_jec3
        phi[counter] = entry.jetAK4_phi3
        muf[counter] = entry.jetAK4_muf3
        nhf[counter] = entry.jetAK4_nhf3
        chf[counter] = entry.jetAK4_chf3
        area[counter] = entry.jetAK4_area3
        nemf[counter] = entry.jetAK4_nemf3
        cemf[counter] = entry.jetAK4_cemf3
        btagDeepFlavB[counter] = entry.jetAK4_btagDeepFlavB3
        nConstituents[counter] = entry.jetAK4_nConstituents3

        counter += 1
        if counter == eventNum:
            break

    np.save(outDirectory+"pt3_values.npy",pt)
    np.save(outDirectory+"y3_values.npy",y)
    np.save(outDirectory+"eta3_values.npy",eta)
    np.save(outDirectory+"m3_values.npy",m)
    np.save(outDirectory+"jec3_values.npy",jec)
    np.save(outDirectory+"muf3_values.npy",muf)
    np.save(outDirectory+"phi3_values.npy",phi)
    np.save(outDirectory+"nhf3_values.npy",nhf)
    np.save(outDirectory+"chf3_values.npy",chf)
    np.save(outDirectory+"area3_values.npy",area)
    np.save(outDirectory+"nemf3_values.npy",nemf)
    np.save(outDirectory+"cemf3_values.npy",cemf)
    np.save(outDirectory+"btagDeepFlavB3_values.npy",btagDeepFlavB)
    np.save(outDirectory+"nConstituents3_values.npy",nConstituents)
    print("Jet 3 numpy arrays saved")

RootDataFolder = "/nfs/dust/cms/user/hinzmann/run2023/"
NumpyFolder = "/nfs/dust/cms/user/mueckejo/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/run2023BM0/Numpy/"
fileName = RootDataFolder+"JetMET0_Run2023B-PromptNanoAODv11p9_v1-v1_NANOAOD.root"
treeName = "Events"
eventNum = 1000000

#loading data and save as numpy arrays from root tree
pt1,eta1,phi1,m1,y1 = loadRootDataJet1(fileName,treeName,eventNum,NumpyFolder)
pt2,eta2,phi2,m2,y2 = loadRootDataJet2(fileName,treeName,eventNum,NumpyFolder)
loadRootDataJet3(fileName,treeName,eventNum,NumpyFolder)

#calculate mjj, chi and yboost and save them as numpy arrays
tempmjj = np.full(eventNum,-999.0)
tempyboost = np.full(eventNum,-999.0)
tempchi = np.full(eventNum,-999.0)
for i in range(0,eventNum):
    if pt1[i] != -999.0 and eta1[i] != -999.0 and phi1[i] != -999.0 and m1[i] != -999.0 and pt2[i] != -999.0 and eta2[i] != -999.0 and phi2[i] != -999.0 and m2[i] != -999.0:
        #calculate mjj
        tempLorentz1 = ROOT.TLorentzVector()
        tempLorentz2 = ROOT.TLorentzVector()
        tempLorentz1.SetPtEtaPhiM(pt1[i],eta1[i],phi1[i],m1[i])
        tempLorentz2.SetPtEtaPhiM(pt2[i],eta2[i],phi2[i],m2[i])
        invarient = tempLorentz1 + tempLorentz2
        tempmjj[i] = invarient.M()
        #calculate yboost
        tempyboost[i] = 1/2*(y1[i]+y2[i])
        #calculate chi
        tempchi[i] = np.exp(abs(y1[i]-y2[i]))
np.save(NumpyFolder+"mjj_values.npy",tempmjj)
np.save(NumpyFolder+"yboost_values.npy",tempyboost)
np.save(NumpyFolder+"chi_values.npy",tempchi)

print("programm finished")
