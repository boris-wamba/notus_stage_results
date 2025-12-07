BEGIN {
        time=0
        MeanKE=0
        MeanP=0
        MeanKEDR=0
        MeanNuT=0
        MeanLesProduction=0
        MeanStrainRate=0 
        }{
  if (NF > 1) {
    if (($1 == "Time") && ($2 == "iteration")) { 
        time=$9
    }
    if (($1 == "Mean") && ($2 == "kinetic") && ($3 == "energy:")) { 
        MeanKE=$4
    }
    if (($1 == "Mean") && ($2 == "pressure:")) { 
        MeanP=$3
    }
    if (($1 == "Mean") && ($2 == "kinetic") && ($3 == "energy") && ($4 == "dissipation")) { 
        MeanKEDR=$6
    }
    if (($1 == "Mean") && ($2 == "turbulent") && ($3 == "viscosity")) { 
        MeanNuT=$5
    }
    if (($1 == "Mean") && ($2 == "strain") && ($3 == "rate") && ($4 == "magnitude:")) { 
        MeanStrainRate=$5 
    }
    if (($1 == "Mean") && ($2 == "les") && ($3 == "production") && ($4 == "term")) { 
        MeanLesProduction=$6
        print time, MeanKE, MeanKEDR, MeanP, MeanNuT, MeanLesProduction, MeanStrainRate
    }
  }
}


