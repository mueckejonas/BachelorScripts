import ROOT

#loading up to 10 root files from a root tree and gives out the hists
#input: FileName,histName1,histName2,histName3,histName4,histName5,histName6,histName7,histName8,histName9,histName10
#output: hist1,hist2,hist3,hist4,hist5,hist6,hist7,hist8,hist9,hist10
def loadRootFiles(FileName,histName1=None,histName2=None,histName3=None,histName4=None,histName5=None,histName6=None,histName7=None,histName8=None,histName9=None,histName10=None):
    histFile = ROOT.TFile.Open(FileName,"READ")

    if histName1 != None:
        hist1 = histFile.Get(histName1)
        hist1.SetDirectory(0)
    else:
        hist1 = None
    if histName2 != None:
        hist2 = histFile.Get(histName2)
        hist2.SetDirectory(0)
    else:
        hist2 = None
    if histName3 != None:
        hist3 = histFile.Get(histName3)
        hist3.SetDirectory(0)
    else:
        hist3 = None
    if histName4 != None:
        hist4 = histFile.Get(histName4)
        hist4.SetDirectory(0)
    else:
        hist4 = None
    if histName5 != None:
        hist5 = histFile.Get(histName5)
        hist5.SetDirectory(0)
    else:
        hist5 = None
    if histName6 != None:
        hist6 = histFile.Get(histName6)
        hist6.SetDirectory(0)
    else:
        hist6 = None
    if histName7 != None:
        hist7 = histFile.Get(histName7)
        hist7.SetDirectory(0)
    else:
        hist7 = None
    if histName8 != None:
        hist8 = histFile.Get(histName8)
        hist8.SetDirectory(0)
    else:
        hist8 = None
    if histName9 != None:
        hist9 = histFile.Get(histName9)
        hist9.SetDirectory(0)
    else:
        hist9 = None
    if histName10 != None:
        hist10 = histFile.Get(histName10)
        hist10.SetDirectory(0)
    else:
        hist10 = None

    histFile.Close()
    print(FileName+" is loaded")
    return hist1,hist2,hist3,hist4,hist5,hist6,hist7,hist8,hist9,hist10

#takes data array of hists and vconverts them into pdf files with custom design settings
#input: outFileName,data,titlesArray,xAxisTitle,yAxisTitle
#output: creates pdf file in outFileName
def RootHisttoPdf(outFileName,data,titlesArray,xAxisTitle,yAxisTitle,histNum,logyScale):
    canvas = ROOT.TCanvas("canvas")
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data[0],"data")

    canvas.Print(outFileName+"[")
    for i in range(0,histNum):
        data[i].SetStats(0)
        data[i].SetLineColor(ROOT.kBlack)
        data[i].SetLineWidth(2)
        data[i].GetYaxis().SetTitle(yAxisTitle)
        data[i].GetXaxis().SetTitle(xAxisTitle)
        data[i].SetTitle("")
        data[i].Draw("pe")
        legend.Draw("same")
        latex.DrawText(0.5,0.8,titlesArray[i])
        canvas.Print(outFileName)
    canvas.Print(outFileName+"]")

#loads hists and create pdf files for certain quantity
def loadAndSave(inDirectory,outDirectory,histNum,variable,xAxis,setLogy=False):
    Hist1,Hist2,Hist3,Hist4,Hist5,Hist6,Hist7,Hist8,Hist9,Hist10 = loadRootFiles(inDirectory+variable+"hists.root",variable+"allmjjvaluesHist",variable+"250to350Hist",variable+"350to500Hist",variable+"500to650Hist",variable+"650to850Hist",variable+"850to1100Hist",variable+"1100to1400Hist",variable+"1400to1800Hist",variable+"1800to2200Hist",variable+"over2200Hist")
    HistArray = [Hist1,Hist2,Hist3,Hist4,Hist5,Hist6,Hist7,Hist8,Hist9,Hist10] #only put the hists you need
    TitlesArray = ["All Mjj [GeV] values","250 < Mjj [GeV] < 350","350 < Mjj [GeV] < 500","500 < Mjj [GeV] < 650","650 < Mjj [GeV] < 850","850 < Mjj [GeV] < 1100","1100 < Mjj [GeV] < 1400","1400 < Mjj [GeV] < 1800","1800 < Mjj [GeV] < 2200","2200 < Mjj [GeV]"]
    #add setLogy to function as last parameter when scale should be logy
    RootHisttoPdf(outDirectory+variable+"hists.pdf",HistArray,TitlesArray,xAxis,"N",histNum,setLogy)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Pdf/Single/"

#create Jet1 pdfs
loadAndSave(inDirectory,outDirectory,10,"pt1","Pt1 [GeV]",True)
loadAndSave(inDirectory,outDirectory,10,"eta1","Eta1")
loadAndSave(inDirectory,outDirectory,10,"y1","Y1")
loadAndSave(inDirectory,outDirectory,10,"phi1","Phi1")
loadAndSave(inDirectory,outDirectory,10,"jec1","Jet energy correction 1")
loadAndSave(inDirectory,outDirectory,10,"muf1","Muon energy fraction 1")
loadAndSave(inDirectory,outDirectory,10,"chf1","Charged energy fraction 1")
loadAndSave(inDirectory,outDirectory,10,"area1","Jet catchement area 1")
loadAndSave(inDirectory,outDirectory,10,"nemf1","Neutral em energy fraction 1")
loadAndSave(inDirectory,outDirectory,10,"cemf1","Charged em energy fraction 1")
loadAndSave(inDirectory,outDirectory,10,"btagDeepFlavB1","DeepJet b+bb+lepb tag discriminator 1")
loadAndSave(inDirectory,outDirectory,10,"nConstituents1","Particles in jet1")
#create Jet2 pdfs
loadAndSave(inDirectory,outDirectory,10,"pt2","Pt2 [GeV]",True)
loadAndSave(inDirectory,outDirectory,10,"eta2","Eta2")
loadAndSave(inDirectory,outDirectory,10,"y2","Y2")
loadAndSave(inDirectory,outDirectory,10,"phi2","Phi2")
loadAndSave(inDirectory,outDirectory,10,"jec2","Jet energy correction 2")
loadAndSave(inDirectory,outDirectory,10,"muf2","Muon energy fraction 2")
loadAndSave(inDirectory,outDirectory,10,"chf2","Charged energy fraction 2")
loadAndSave(inDirectory,outDirectory,10,"area2","Jet catchement area 2")
loadAndSave(inDirectory,outDirectory,10,"nemf2","Neutral em energy fraction 2")
loadAndSave(inDirectory,outDirectory,10,"cemf2","Charged em energy fraction 2")
loadAndSave(inDirectory,outDirectory,10,"btagDeepFlavB2","DeepJet b+bb+lepb tag discriminator 2")
loadAndSave(inDirectory,outDirectory,10,"nConstituents2","Particles in jet2")
#create Jet3 pdfs
loadAndSave(inDirectory,outDirectory,10,"pt3","Pt3 [GeV]",True)
loadAndSave(inDirectory,outDirectory,10,"eta3","Eta3")
loadAndSave(inDirectory,outDirectory,10,"y3","Y3")
loadAndSave(inDirectory,outDirectory,10,"phi3","Phi3")
loadAndSave(inDirectory,outDirectory,10,"jec3","Jet energy correction 3")
loadAndSave(inDirectory,outDirectory,10,"muf3","Muon energy fraction 3")
loadAndSave(inDirectory,outDirectory,10,"chf3","Charged energy fraction 3")
loadAndSave(inDirectory,outDirectory,10,"area3","Jet catchement area 3")
loadAndSave(inDirectory,outDirectory,10,"nemf3","Neutral em energy fraction 3")
loadAndSave(inDirectory,outDirectory,10,"cemf3","Charged em energy fraction 3")
loadAndSave(inDirectory,outDirectory,10,"btagDeepFlavB3","DeepJet b+bb+lepb tag discriminator 3")
loadAndSave(inDirectory,outDirectory,10,"nConstituents3","Particles in jet3")
#create general pdfs
loadAndSave(inDirectory,outDirectory,10,"yboost","yboost [GeV]",True)
loadAndSave(inDirectory,outDirectory,10,"chi","chi [GeV]",True)
#create mjj pdf
mjjHist1,mjjHist2,mjjHist3,mjjHist4,mjjHist5,mjjHist6,mjjHist7,mjjHist8,mjjHist9,mjjHist10 = loadRootFiles(inDirectory+"mjjhists.root","mjj hist")
mjjHistArray = [mjjHist1] #only put the hists you need
mjjTitlesArray = ["All Mjj [GeV] values"]
histNum = 1 #put number of mjjHistArray length
#add setLogy to function as last parameter when scale should be logy
RootHisttoPdf(outDirectory+"mjjhists.pdf",mjjHistArray,mjjTitlesArray,"Mjj [GeV]","N",histNum,True)
