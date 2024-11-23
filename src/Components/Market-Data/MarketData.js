import React    from "react";
import template from "./MarketData.jsx";

class MarketData extends React.Component {
  render() {
    return template.call(this);
  }
}

export default MarketData;
