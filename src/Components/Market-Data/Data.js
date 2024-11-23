import React, { useState, useEffect } from "react";
import {Graph} from "./Graph";

export default function Data(){
    const [data, setData] = useState(null);
    function getData()
    {
        const companyName = document.getElementById("companyName").value;
        console.log("company name", companyName);

        fetch("http://127.0.0.1:5000/stock" + companyName)
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            setData(data);
        })
        .catch((error) => {
            console.log("error", error);
        })

        return(
            <div>
                <input type="text" id="companyName" placeholder="Search Company"/>
                <button onClick={() => getData()}> Data</button>
                <Graph data={data === null ? {'2024-08-01 16:00:00': 1}: data['data']}/>
            </div>
        )
    }
}