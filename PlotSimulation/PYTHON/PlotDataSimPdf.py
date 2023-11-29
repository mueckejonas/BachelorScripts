import ROOT
import numpy as np

#takes three hists and turn them into pdf
def RootHisttoPdf(outFileName,data,simulation,logyScale,yAxisTitle,xAxisTitle,title,undertitle):
    canvas_pads = ROOT.TCanvas("canvas_pads", "Double ratio")
    pad_top = ROOT.TPad("top_pad", "Top pad", 0, 0.3, 1, 1)
    if logyScale:
        pad_top.SetLogy(True)
    pad_top.SetBottomMargin(0)
    pad_top.Draw()
    pad_bottom = ROOT.TPad("bottom_pad", "Bottom pad", 0, 0.05, 1, 0.3)
    pad_bottom.SetBottomMargin(0.25)
    pad_bottom.SetTopMargin(0)
    pad_bottom.Draw()

    latex = ROOT.TLatex()
    latex.SetNDC()
    latex.SetTextSize(0.06)

    legend = ROOT.TLegend(0.7,0.6,0.85,0.75)
    legend.SetLineWidth(0)
    legend.SetTextSize(0.03)
    legend.AddEntry(data,"Data")
    legend.AddEntry(simulation,"Simulation (*Integral_{data}/Integral_{sim})")

    line = ROOT.TLine(data.GetXaxis().GetXmin(),1,data.GetXaxis().GetXmax(),1)
    line.SetLineColor(ROOT.kBlack)
    line.SetLineWidth(2)

    #create and draw to upper plot
    pad_top.cd()
    data.SetStats(0)
    data.SetLineColor(ROOT.kBlack)
    data.SetLineWidth(2)
    simulation.SetStats(0)
    simulation.SetLineColor(ROOT.kRed)
    simulation.SetLineWidth(2)
    simulation.SetTitle("")
    data.GetYaxis().SetTitle(yAxisTitle)
    data.GetYaxis().SetTitleSize(0.05)
    data.GetXaxis().SetTitleSize(0)
    data.GetXaxis().SetLabelSize(0)
    data.SetTitle("")
    data.Scale(1/1.206)
    simulation.Scale(data.Integral()/simulation.Integral())
    data.Draw("pe")
    simulation.Draw("h,same")
    legend.Draw("same")
    latex.DrawText(0.7,0.83,title)
    latex.SetTextSize(0.04)
    latex.DrawText(0.7,0.77,undertitle)
    #create and draw to bottom plot
    pad_bottom.cd()
    ratioDataSim = data.Clone()
    ratioDataSim.Divide(simulation)
    ratioDataSim.SetLineColor(ROOT.kBlack)
    ratioDataSim.SetLineWidth(2)
    ratioDataSim.SetTitle("")
    ratioDataSim.GetYaxis().SetTitle("Data/Simulation")
    ratioDataSim.GetYaxis().SetLabelSize(0.1)
    ratioDataSim.GetYaxis().SetTitleSize(0.15)
    ratioDataSim.GetXaxis().SetLabelSize(0.12)
    ratioDataSim.GetXaxis().SetTitleSize(0.12)
    ratioDataSim.GetYaxis().SetTitleOffset(0.3)
    ratioDataSim.GetYaxis().SetNdivisions (207)
    ratioDataSim.GetXaxis().SetTitle(xAxisTitle)
    ratioDataSim.GetYaxis().SetRangeUser(0.5,1.5)
    ratioDataSim.SetLineColor(ROOT.kRed)
    ratioDataSim.Draw("pe")
    line.Draw("same")
    #draw whole plot
    canvas_pads.Draw()
    canvas_pads.Print(outFileName)



#define directories
dataInDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/DijetEventSelection/ROOT/"
simInDirectory ="/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/ROOT/"
outDirectory = "/home/jmuecke/code/mueckejonas/BachelorArbeitJM/BachelorStorage/PlotSimulation/PDF/RatioPlot/DataSimulation/"
dataInFileName = dataInDirectory+"Hists_Run2023B.root"
simInFileName = simInDirectory+"Run3SimulationWithWeigth.root"

#Get data Jets and Kinematics
dataHistFile = ROOT.TFile.Open(dataInFileName,"READ")
dataJet1 = dataHistFile.Get("Jet1Data")
dataJet2 = dataHistFile.Get("Jet2Data")
dataJet3 = dataHistFile.Get("Jet3Data")
dataKinematics = dataHistFile.Get("Kinematics")

#Get Sim Jets and Kinematics
simHistFile = ROOT.TFile.Open(simInFileName,"READ")
simJet1 = simHistFile.Get("simJet1")
simJet2 = simHistFile.Get("simJet2")
simJet3 = simHistFile.Get("simJet3")
simKinematics = simHistFile.Get("simKinematics")

#define variables to compare and plot as array
JetNameArray = np.array(["pt","y","eta","phi","mass","jec","muf","nhf","chf","area","nemf","cemf","btagDeepFlavB","nConstituents"])
XaxisArray = np.array(["Pt [GeV]","Y","Eta","Phi","Mass [Gev]","Jec","Muf","Nhf","Chf","Area","Nemf","Cemf","BtagDeepFlavB","NConstituents"])

#create data and simulation ratio plots pdfs
for i in range(0,14):
    #get data
    data1 = dataJet1.Get("data"+JetNameArray[i]+"1")
    data2 = dataJet2.Get("data"+JetNameArray[i]+"2")
    data3 = dataJet3.Get("data"+JetNameArray[i]+"3")

    #get simulation
    sim1 = simJet1.Get(JetNameArray[i]+"1sim_hist")
    sim2 = simJet2.Get(JetNameArray[i]+"2sim_hist")
    sim3 = simJet3.Get(JetNameArray[i]+"3sim_hist")

    #create and save pdf files
    if JetNameArray[i] == "pt" or JetNameArray[i] == "mass":
        RootHisttoPdf(outDirectory+JetNameArray[i]+"1DataandSim.pdf",data1,sim1,True,"#sigma [pb]",XaxisArray[i],"Run3 2023",JetNameArray[i]+" Jet1")
        RootHisttoPdf(outDirectory+JetNameArray[i]+"2DataandSim.pdf",data2,sim2,True,"#sigma [pb]",XaxisArray[i],"Run3 2023",JetNameArray[i]+" Jet2")
        RootHisttoPdf(outDirectory+JetNameArray[i]+"3DataandSim.pdf",data3,sim3,True,"#sigma [pb]",XaxisArray[i],"Run3 2023",JetNameArray[i]+" Jet3")
    else:
        RootHisttoPdf(outDirectory+JetNameArray[i]+"1DataandSim.pdf",data1,sim1,False,"#sigma [pb]",XaxisArray[i],"Run3 2023",JetNameArray[i]+" Jet1")
        RootHisttoPdf(outDirectory+JetNameArray[i]+"2DataandSim.pdf",data2,sim2,False,"#sigma [pb]",XaxisArray[i],"Run3 2023",JetNameArray[i]+" Jet2")
        RootHisttoPdf(outDirectory+JetNameArray[i]+"3DataandSim.pdf",data3,sim3,False,"#sigma [pb]",XaxisArray[i],"Run3 2023",JetNameArray[i]+" Jet3")


#create yboost pdf
datayboost = dataKinematics.Get("datayboost")
simyboost = simKinematics.Get("yboostsim_hist")
RootHisttoPdf(outDirectory+"yboostDataandSim.pdf",datayboost,simyboost,False,"#sigma [pb]","Yboost","Run3 2023","Yboost")
#create chi pdf
datachi = dataKinematics.Get("datachi")
simchi = simKinematics.Get("chisim_hist")
RootHisttoPdf(outDirectory+"chiDataandSim.pdf",datachi,simchi,False,"#sigma [pb]","Chi","Run3 2023","Chi")
#create mjj pdf
datamjj = dataKinematics.Get("datamjj")
simmjj = simKinematics.Get("mjjsim_hist")
RootHisttoPdf(outDirectory+"mjjDataandSim.pdf",datamjj,simmjj,True,"#sigma [pb]","Mjj [GeV]","Run3 2023","Mjj")
