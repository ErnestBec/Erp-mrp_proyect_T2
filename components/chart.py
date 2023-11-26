
def newChart(label:str,data,hexColor:str):
    return "{ label: '"+label+"', data: "+str(data)+", fill: false, borderColor: '"+hexColor+"', tension: 0, clip: true, hoverBorderWidth: 8, pointHitRadius: 50, pointRadius: 3, pointBorderWidth: 4 }"
