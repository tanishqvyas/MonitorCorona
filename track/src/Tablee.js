import React from 'react';
import axios from 'axios';



class Location extends React.Component {
    render() {
        var locstyle = {
            paddingTop: 12,
            paddingRight: 16,
            paddingBottom: 12,
            paddingLeft: 0,
            display: "inlineBlock",
            width : "800px"
        }

        var logostyle = {
            maxHeight: "16px",
            minHeight: "16px",
            maxWidth: "16px",
            minWidth: "16px",
            marginRight: "12px"
        }

        return (
            <td style={locstyle}>
                <img style={logostyle} src={this.props.flag} onError={(e)=>{e.target.onerror = null; e.target.src="world.jpeg"}} />
                {this.props.loc}
            </td>
        )
    }
}

class Confirmed extends React.Component {
    render() {
        var confstyle = {
            paddingTop: 12,
            paddingRight: 16,
            paddingBottom: 12,
            paddingLeft: 16,
            // display:"inlineBlock",    
        }

        return (
            <td style={confstyle}>
                {this.props.conf}
            </td>
        )
    }
}

class Cases_per1M extends React.Component {
    render() {
        var casesstyle = {
            paddingTop: 12,
            paddingRight: 16,
            paddingBottom: 12,
            paddingLeft: 16,
            // display:"inlineBlock"    
        }

        return (
            <td style={casesstyle}>
                {this.props.cpm}
            </td>
        )
    }
}

class Recovered extends React.Component {
    render() {
        var recoveredstyle = {
            paddingTop: 12,
            paddingRight: 16,
            paddingBottom: 12,
            paddingLeft: 16,
            // display:"inlineBlock"    
        }

        return (
            <td style={recoveredstyle}>
                {this.props.r}
            </td>
        )
    }
}

class Deaths extends React.Component {
    render() {
        var deathsstyle = {
            paddingTop: 12,
            paddingRight: 16,
            paddingBottom: 12,
            paddingLeft: 16,
            // display:"inlineBlock"                   
        }

        return (
            <td style={deathsstyle}>
                {this.props.d}
            </td>
        )
    }
}




class TableComponent extends React.Component {

    // state = {
    //     dataRows:[]
    // }

    // componentDidMount() {
    //     axios.get('http://127.0.0.1:7000/api/')
    //         .then(res=>{
    //             this.setState({
    //                 dataRows: res.data
    //             });
                
    //             // console.log(res.data);
    //         })

    // }
    


    render() {

        var dataRows = this.props.data;
            
        // var dataRows = rowData;
        // var dataColumns=['cname','ccases','ccasespm','totalrecovered','totaldeaths']
        
        var rowstyle = {
            borderTop: "1px solid",
            display: "inlineBlock"
        }


        var tableHeaders = (
            <thead>
                <tr>
                    <th> Locations </th>
                    <th id="cases"> Confirmed <span id="arrows"><span id="arrow-up"></span>
                                                <span id="arrow-down"></span></span></th>
                    <th> Cases per 1M people   </th>
                    <th> Recovered </th>
                    <th> Deaths </th>

                </tr>
            </thead>
        );

        var tableBody = dataRows.map(function (row) {
            return (

                <tr style={rowstyle}>
                    <Location loc={row.country_name} flag={row.url} />
                    <Confirmed conf={row.confirmed_cases} />
                    <Cases_per1M cpm={row.cases_per_million} />
                    <Recovered r={row.total_recovered} />
                    <Deaths d={row.total_deaths} />

                </tr>
            );
        });

        return (<table id="MyTable" class='tableclass'>
            {tableHeaders}
            <tbody>
                {tableBody}
            </tbody>
        </table>

        );
    }
}





class GlobalSearchComponent extends React.Component {
constructor(props) {
super(props);
this.state = {
    filteredData: [],
    columnSearch: "",
    searchInput: ""
    };
    }

handleChange = event => {
const val = event.target.value;
this.setState({ searchInput: val }, () => this.globalSearch());
this.props.handleSetSearchInput(val);
};

globalSearch = () => {
const { searchInput, columnSearch } = this.state;
let filteredData = this.props.data.filter(value => {
if (columnSearch) {
return value[columnSearch]
  .toString()
  .toLowerCase()
  .includes(searchInput.toLowerCase());
}
return (
value.country_name.toLowerCase().includes(searchInput.toLowerCase())
);
});

this.props.handleSetFilteredData(filteredData);
};

setColumnSearch = e => {
this.setState({ columnSearch: e.target.value }, () => this.globalSearch());
};

render() {
const { columns } = this.props;
const { columnSearch } = this.state;

return (
<div>
<br />
<input type="text"
  name="searchInput"
  placeholder = "Search"
  value={this.state.searchInput || ""}
  onChange={this.handleChange}
  label="Search"
  id="searchtab"
/>
<select id="selectdropdown"
  onChange={e => {
    e.persist();
    this.setColumnSearch(e);
  }}
  value={columnSearch}
>
  <option value=""> All columns</option>
  {columns.map(col => {
    return <option value={col.accessor}>{col.Header}</option>;
  })}
</select>
<br />
<br />
</div>
);
}
}



class Tablee extends React.Component {
constructor(props) {
    super(props);
    this.state = {
    data: [],
    filteredData: [],
    columns: [],
    searchInput: ""
    };
}

componentDidMount() {
    this.getData();
    this.getColumns();
}

getColumns = () => {
    let columns = [
    {
        Header: "Locations",
        accessor: "country_name",
        sortable: false,
        show: true,
        displayValue: "Locations"
    },
    {
        Header: "Confirmed",
        accessor: "confirmed_cases",
        sortable: false,
        show: true,
        displayValue: "Confirmed"
    },
    {
        Header: "Cases per 1M people",
        accessor: "cases_per_million",
        sortable: false,
        show: true,
        displayValue: "Cases per 1M people"
    },
    {
        Header: "Recovered",
        accessor: "total_recovered",
        sortable: false,
        show: true,
        displayValue: "Recovered"
    },
    {
        Header: "Deaths",
        accessor: "total_deaths",
        sortable: false,
        show: true,
        displayValue: "Deaths"
    }
    ];
    this.setState({ columns });
};

getData = () => {
    let data =rowData;
    this.setState({ data });
};

handleSetData = data => {
    console.log(data);
    this.setState({ data });
};

handleSetFilteredData = filteredData => {
    this.setState({ filteredData });
};

handleSetSearchInput = searchInput => {
    this.setState({ searchInput });
};

render() {
    let { data, filteredData, columns, searchInput } = this.state;
    const dataToDisplay = searchInput.length ? filteredData : data;
    return (
    <div>
        <GlobalSearchComponent
        data={this.state.data}
        columns={this.state.columns}
        handleSetFilteredData={this.handleSetFilteredData}
        handleSetSearchInput={this.handleSetSearchInput}
        />
        <TableComponent data={dataToDisplay}/>
    </div>
    );
}
}


// var query_results = []

// axios.get('http://127.0.0.1:7000/api/')
//     .then(res=>{
//         query_results= res.data
//         console.log(res.data)
//     })


 var rowData =[]


    // state = {
    //     dataRows:[]
    // }

    // componentDidMount() {
    //     axios.get('http://127.0.0.1:7000/api/')
    //         .then(function(res){

    //                 rowData=res.data;
            
    //             console.log("this is res data")
    //             console.log(res.data);
    //         });
    //         console.log("this is row data")
    //         console.log(rowData);
    // // }




    function getData(){
        var strr = [];
        axios.get('http://127.0.0.1:8000/api/')
       .then(function(response){
               strr.push(...response.data);
        })
        return strr;

    }
    var rowData=getData()
    // rowData=rowData[0]
    console.log(rowData)
// var destination = document.querySelector("#innercontainer")
// {% for item in query_results %}
// var san = {
//     'cname': "{{item.country_name}}",
//     'ccases': "{{ item.confirmed_cases }}",
//     'ccasespm': "{{ item.cases_per_million }}",
//     'totalrecovered': "{{item.total_recovered}}",
//     'totaldeaths': "{{item.total_deaths}}",
//     'flaglogo': "{{item.url}}"
// }
// rowData.push(san)
// {% endfor %}


window.onload = function(){
    var a = document.getElementById("arrow-up");
    var b = document.getElementById("arrow-down");
        
    var c=document.getElementById("cases");


    c.onclick=sortTable;
    function sortTable() {
      var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
      table = document.getElementById("MyTable");
      switching = true;
      //Set the sorting direction to ascending:
      dir = "asc"; 
      
      a.style.display = "block";
        b.style.display="none";
      /*Make a loop that will continue until
      no switching has been done:*/
      while (switching) {
        //start by saying: no switching is done:
        switching = false;
        rows = table.rows;
        /*Loop through all table rows (except the
        first, which contains table headers):*/
        for (i = 1; i < (rows.length - 1); i++) {
          //start by saying there should be no switching:
          shouldSwitch = false;
          /*Get the two elements you want to compare,
          one from current row and one from the next:*/
          x = rows[i].getElementsByTagName("td")[1];
          y = rows[i + 1].getElementsByTagName("td")[1];
          /*check if the two rows should switch place,
          based on the direction, asc or desc:*/
          if (dir == "asc") {
            
            if (parseInt(x.innerHTML)> parseInt(y.innerHTML)) {
              //if so, mark as a switch and break the loop:
              shouldSwitch= true;
              break;
            }
          } else if (dir == "desc") {
              
        
            if (parseInt(x.innerHTML) <parseInt(y.innerHTML)) {
              //if so, mark as a switch and break the loop:
              shouldSwitch = true;
              break;
            }
          }
        }
        if (shouldSwitch) {
          /*If a switch has been marked, make the switch
          and mark that a switch has been done:*/
          rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
          switching = true;
          //Each time a switch is done, increase this count by 1:
          switchcount ++;      
        } else {
          /*If no switching has been done AND the direction is "asc",
          set the direction to "desc" and run the while loop again.*/
          if (switchcount == 0 && dir == "asc") {
            a.style.display = "none";
            b.style.display = "block";
            dir = "desc";
            switching = true;
          }
        }
      }
    }
        };

export default Tablee;