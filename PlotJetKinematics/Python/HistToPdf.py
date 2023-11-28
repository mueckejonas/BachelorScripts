import ROOT
import numpy as np
#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data1,logyScale,dataNumber,yAxisTitle,xAxisTitle,title,data2=None,data3=None,dataName="Jet1 data"):
    canvas = ROOT.TCanvas("canvas")
    if logyScale:
        canvas.SetLogy(True)
    canvas.cd()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.03)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.AddEntry(data1,dataName)
    if dataNumber > 2:
        legend.AddEntry(data2,"Jet2 data")
        legend.AddEntry(data3,"Jet3 data")
    else:
        legend.SetTextSize(0.03)

    data1.SetStats(0)
    data1.SetLineColor(ROOT.kBlack)
    data1.SetLineWidth(2)
    if dataNumber > 2:
        data2.SetStats(0)
        data2.SetLineColor(ROOT.kBlue)
        data2.SetLineWidth(2)
        data3.SetStats(0)
        data3.SetLineColor(ROOT.kRed)
        data3.SetLineWidth(2)
        data2.SetTitle("")
        data3.SetTitle("")
    data1.GetYaxis().SetTitle(yAxisTitle)
    data1.GetXaxis().SetTitle(xAxisTitle)
    data1.SetTitle("")
    data1.Draw("pe")
    if dataNumber > 2:
        data2.Draw("pe,same")
        data3.Draw("pe,same")
    legend.Draw("same")
    latex.DrawText(0.7,0.8,title)
    canvas.Print(outFileName)

#define directory
inDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Root/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotJetKInematics/Pdf/Together/"
inFileName = inDirectory+"Hists_Run2023B.root"
#Get Jets and Kinematics
histFile = ROOT.TFile.Open(inFileName,"READ")
Jet1 = histFile.Get("Jet1Data")
Jet2 = histFile.Get("Jet2Data")
Jet3 = histFile.Get("Jet3Data")
Kinematics = histFile.Get("Kinematics")

JetNameArray = np.array(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents","yboost","chi","mjj"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])

#create Jet pdfs
for i in range(0,14):
    data1 = Jet1.Get("data"+JetNameArray[i]+"1")
    data2 = Jet2.Get("data"+JetNameArray[i]+"2")
    data3 = Jet3.Get("data"+JetNameArray[i]+"3")

    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+JetNameArray[i]+".pdf",data1,True,3,"N",XaxisArray[i],XaxisArray[i]+" values",data2,data3)
    else:
        RootHisttoPdf(outDirectory+JetNameArray[i]+".pdf",data1,False,3,"N",XaxisArray[i],XaxisArray[i]+" values",data2,data3)

#create yboost pdf
yboostData = Kinematics.Get("datayboost")
RootHisttoPdf(outDirectory+"yboost.pdf",yboostData,False,1,"N","Yboost","Yboost values",None,None,"Yboost")
#create chi pdf
chiData = Kinematics.Get("datachi")
RootHisttoPdf(outDirectory+"chi.pdf",chiData,False,1,"N","Chi","Chi values",None,None,"Chi")
#create mjj pdf
mjjData = Kinematics.Get("datamjj")
RootHisttoPdf(outDirectory+"mjj.pdf",mjjData,True,1,"N","Mjj [GeV]","Mjj values",None,None,"Mjj")
