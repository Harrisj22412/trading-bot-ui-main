/* eslint-disable no-undef */
/* eslint-disable no-unused-vars */
import { react } from "react";

const TradeControls = ({ onTradeParamsChange }) => {
    const [asset, setAsset ] = useState('');
    const [entryPrice, setEntryPrice ] = useState(0);
    const [stopLoss, setStopLoss ] = useState(0);
    const [quantity, setQuantity ] = useState(0);

    const handleAssetChange = (event) => {
        setAsset(event.target.value);
    }

    const handleStopLossChange = (event) => {
        setStopLoss(parseFloat(event.target.value));
    }

    const handleQuantityChange = (event) => {
        setQuantity(parseInt(event.target.value));
    }

    const handleSubmit = (event) => {
        event.preventDefault();

        onTradeParamsChange({ asset, entryPrice, stopLoss,  quantity});
    };
}