function ajaxGetRequest(path, callback) {
  let request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (this.readyState===4 && this.status ===200) {
      callback(this.response);
      }
    }
    request.open("GET", path);
    request.send();
}
function showScatter(response) { 
 let data = JSON.parse(response);
 let trace1 = {
   x: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,
   23,24,25,26,27,28,29,30,31,32],
   y: data,
   mode: 'markers',
   type: 'scatter'
 }
 let results = [trace1];
 let layout = {
   xaxis: {
     range: [0,32],
     title: 'Day of the Month'
   },
   yaxis: {
     range: [0,400],
     title: '# Tows'
   },
   title: "Tows by Day of the Month" 
 };
 Plotly.newPlot('scatter',results,layout);
}

function showPie(response) {
  let data = JSON.parse(response);
  let info = [{
    values: data,
    labels: ['District A', 'District B', 'District C', 'District D',
    'District E'],
    type: 'pie'
  }];
  let layout = {
    height: 400,
    width: 500,
    title: "Tows by District"
  };
  Plotly.newPlot('pie',info,layout);
}

function showLine(response) {
  let data = JSON.parse(response);
  trace1 = {
  type: 'scatter',
  x: ['Jan','Feb','Mar','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
  y: data[0],
  mode: 'lines',
  name: 'ILLEGAL VEHICLE',
  line: {
    width: 3
  }
};

  trace2 = {
  type: 'scatter',
  x: ['Jan','Feb','Mar','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
  y: data[1],
  mode: 'lines',
  name: 'ACCIDENT',
  line: {
    width: 3
  }
};
  trace3 = {
    type: 'scatter',
    x: ['Jan','Feb','Mar','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: data[2],
    mode: 'lines',
    name: 'ABANDONED VEHICLE',
    line: {
      width: 3
    }
  };
  trace4 = {
    type: 'scatter',
    x: ['Jan','Feb','Mar','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: data[3],
    mode: 'lines',
    name: 'STOLEN VEHICLE',
    line: {
      width: 3
    }
  };
  trace5 = {
    type: 'scatter',
    x: ['Jan','Feb','Mar','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: data[4],
    mode: 'lines',
    name: 'ILLEGALLY PARKED',
    line: {
      width: 3
    }
  };
  trace6 = {
    type: 'scatter',
    x: ['Jan','Feb','Mar','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: data[5],
    mode: 'lines',
    name: 'IMPOUNDED',
    line: {
      width: 3
    }
   };
  trace7 = {
    type: 'scatter',
    x: ['Jan','Feb','Mar','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
    y: data[6],
    mode: 'lines',
    name: 'GONE ON ARRIVAL', 
    line: {
      width: 3
    }
  };
  let layout = {
  title: '# Tows by Month and Description',
  xaxis: { 
  title: 'Month'
  },
  yaxis: {
    title: '# Tows'
  },
  width: 1000,
  height: 500
};

  let info = [trace1, trace2, trace3, trace4, trace5, trace6, trace7];

Plotly.newPlot('line', info, layout);
}

function getData(){
  ajaxGetRequest("/towsByDay", showScatter);
  ajaxGetRequest("/towsByDistrict", showPie);
  ajaxGetRequest("/towsByDescription", showLine);
}