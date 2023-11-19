import ROOT
import numpy as np

#takes an data array as input and categorize the array by mjj values
def createCategoryHists(data,mjj,eventNum):
    mjj250to350 = np.full(eventNum,-999.0)
    mjj350to500 = np.full(eventNum,-999.0)
    mjj500to650 = np.full(eventNum,-999.0)
    mjj650to850 = np.full(eventNum,-999.0)
    mjj850to1100 = np.full(eventNum,-999.0)
    mjj1100to1400 = np.full(eventNum,-999.0)
    mjj1400to1800 = np.full(eventNum,-999.0)
    mjj1800to2200 = np.full(eventNum,-999.0)
    mjjover2200 = np.full(eventNum,-999.0)

    for i in range(0,data.size):
        if 250 < mjj[i] < 350:
            mjj250to350[i] = data[i]
        elif 350 < mjj[i] < 500:
            mjj350to500[i] = data[i]
        elif 500 < mjj[i] < 650:
            mjj500to650[i] = data[i]
        elif 650 < mjj[i] < 850:
            mjj650to850[i] = data[i]
        elif 850 < mjj[i] < 1100:
            mjj850to1100[i] = data[i]
        elif 1100 < mjj[i] < 1400:
            mjj1100to1400[i] = data[i]
        elif 1400 < mjj[i] < 1800:
            mjj1400to1800[i] = data[i]
        elif 1800 < mjj[i] < 2200:
            mjj1800to2200[i] = data[i]
        elif 2200 < mjj[i]:
            mjjover2200[i] = data[i]
    return mjj250to350,mjj350to500,mjj500to650,mjj650to850,mjj850to1100,mjj1100to1400,mjj1400to1800,mjj1800to2200,mjjover2200

#takes up to 14 hists as input and saves them in an root file
def writeHists(outFileName,hist1=None,hist2=None,hist3=None,hist4=None,hist5=None,hist6=None,hist7=None,hist8=None,hist9=None,hist10=None,hist11=None,hist12=None,hist13=None,hist14=None):
    outHistFile = ROOT.TFile.Open(outFileName,"RECREATE")
    outHistFile.cd()
    if hist1 != None:
        hist1.Write()
    if hist2 != None:
        hist2.Write()
    if hist3 != None:
        hist3.Write()
    if hist4 != None:
        hist4.Write()
    if hist5 != None:
        hist5.Write()
    if hist6 != None:
        hist6.Write()
    if hist7 != None:
        hist7.Write()
    if hist8 != None:
        hist8.Write()
    if hist9 != None:
        hist9.Write()
    if hist10 != None:
        hist10.Write()
    if hist11 != None:
        hist11.Write()
    if hist12 != None:
        hist12.Write()
    if hist13 != None:
        hist13.Write()
    if hist14 != None:
        hist14.Write()
    outHistFile.Close()
    print(outFileName+"created")

#takes an array as input and creates an root hist file
def ArraytoRootHist(data,histName,histTitle,histBinNummer,histXmin,histXmax):
    #TH1D(name,title,binnummer,xmin,xmax)
    temp_hist = ROOT.TH1D(histName,histTitle,histBinNummer,histXmin,histXmax)
    temp_hist.Sumw2()

    for i in range(0,data.size):
        if data[i] != -999.0:
            temp_hist.Fill(data[i])

    temp_hist.SetDirectory(0)
    print("created"+histName)
    return temp_hist

#takes dataname as input and saves the data
def loadAndSaveData(inFileName,outFileName,evNum,mjj,variable,binNum,histXmin,histXmax):
    dataArray = np.load(inFileName+variable+"_values.npy")
    mjj250to350,mjj350to500,mjj500to650,mjj650to850,mjj850to1100,mjj1100to1400,mjj1400to1800,mjj1800to2200,mjjover2200 = createCategoryHists(dataArray,mjj,evNum)
    temphistallmjj = ArraytoRootHist(dataArray,variable+"allmjjvaluesHist",variable+" values",binNum,histXmin,histXmax)
    temp250to350Hist = ArraytoRootHist(mjj250to350,variable+"250to350Hist",variable+" values",binNum,histXmin,histXmax)
    temp350to500Hist = ArraytoRootHist(mjj350to500,variable+"350to500Hist",variable+" values",binNum,histXmin,histXmax)
    temp500to650Hist = ArraytoRootHist(mjj500to650,variable+"500to650Hist",variable+" values",binNum,histXmin,histXmax)
    temp650to850Hist = ArraytoRootHist(mjj650to850,variable+"650to850Hist",variable+" values",binNum,histXmin,histXmax)
    temp850to1100Hist = ArraytoRootHist(mjj850to1100,variable+"850to1100Hist",variable+" values",binNum,histXmin,histXmax)
    temp1100to1400Hist = ArraytoRootHist(mjj1100to1400,variable+"1100to1400Hist",variable+" values",binNum,histXmin,histXmax)
    temp1400to1800Hist = ArraytoRootHist(mjj1400to1800,variable+"1400to1800Hist",variable+" values",binNum,histXmin,histXmax)
    temp1800to2200Hist = ArraytoRootHist(mjj1800to2200,variable+"1800to2200Hist",variable+" values",binNum,histXmin,histXmax)
    tempover2200Hist = ArraytoRootHist(mjjover2200,variable+"over2200Hist",variable+" values",binNum,histXmin,histXmax)
    writeHists(outFileName+variable+"hists.root",temp250to350Hist,temp350to500Hist,temp500to650Hist,temp650to850Hist,temp850to1100Hist,temp1100to1400Hist,temp1400to1800Hist,temp1800to2200Hist,tempover2200Hist,temphistallmjj)

#define general parameters to use
RootFolder = "/nfs/dust/cms/user/mueckejo/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/run2023BM0/Root/"
NumpyFolder = "/nfs/dust/cms/user/mueckejo/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/run2023BM0/Numpy/"
eventNum = 1000000
mjj = np.load(NumpyFolder+"mjj_values.npy")

#load create and save hists
#Jet1
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"pt1",50,0,1000)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"y1",50,-6,6)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"eta1",50,-6,6)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"phi1",50,-4,4)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"m1",50,0,200)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"jec1",50,0.5,1.3)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"muf1",50,0,0.15)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nhf1",50,0,0.4)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"chf1",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"area1",50,0.2,0.8)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nemf1",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"cemf1",50,0,0.15)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"btagDeepFlavB1",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nConstituents1",50,0,100)
#Jet2
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"pt2",50,0,1000)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"y2",50,-6,6)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"eta2",50,-6,6)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"phi2",50,-4,4)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"m2",50,0,200)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"jec2",50,0.5,1.3)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"muf2",50,0,0.15)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nhf2",50,0,0.4)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"chf2",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"area2",50,0.2,0.8)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nemf2",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"cemf2",50,0,0.15)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"btagDeepFlavB2",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nConstituents2",50,0,100)
#general quantities
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"chi",50,0,20)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"yboost",50,0,2)
#mjj values
temp_mjj = ArraytoRootHist(mjj,"mjj hist","mjj values",50,0,5000)
writeHists(RootFolder+"mjjhists.root",temp_mjj)
#Jet3
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"pt3",50,0,1000)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"y3",50,-6,6)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"eta3",50,-6,6)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"phi3",50,-4,4)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"m3",50,0,200)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"jec3",50,0.5,1.3)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"muf3",50,0,0.15)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nhf3",50,0,0.4)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"chf3",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"area3",50,0.2,0.8)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nemf3",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"cemf3",50,0,0.15)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"btagDeepFlavB3",50,0,1)
loadAndSaveData(NumpyFolder,RootFolder,eventNum,mjj,"nConstituents3",50,0,100)
