import './checkoutAd.scss';
import { useStateValue } from './StateProvider';

const CheckoutAd = () => {
  const { myReducer } = useStateValue();
  const [ data ] = myReducer;

  const getTotalAmount = () => {
    let total = 0;
    data.cartList.map(item =>{
      return total = Number(total) + Number(item.price);
    })
    return total;
  }

  const getTotalItem = () => {
    return data.cartList.length
  }

  return(
    <div className="checkoutAd">
      <div className='leftSide'>
        <img src="https://tolleson.com/wp-content/uploads/2017/07/cisco-brand-logo-white-gradient-background.jpg" alt=""/>
      </div>
      <div className="rightSide">
        <div className="subtotal">
          <p>Subtotal({getTotalItem()} items): <strong>${getTotalAmount()}</strong></p>
          <p><input type="checkbox"/>This order contains a gift</p>
          <button>Proceed to Checkout</button>
        </div>
      </div>
    </div>
  )
}

export default CheckoutAd;