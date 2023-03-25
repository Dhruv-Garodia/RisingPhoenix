import { useStateValue } from './StateProvider';
import Rating from './Rating';
const Card = (props) => {
  const { title, price, rating, imageURL } = props;
  const { myReducer } = useStateValue();
  const [ , dispatch] = myReducer;
  const addToCard = (selectedValue) => {
    let timeStamp =  new Date().getTime();
    selectedValue = {...selectedValue, id:timeStamp};
    dispatch({
      type:'ADD_TO_CART',
      payload: selectedValue
    });
  }
  return(
    <div className='Card'>
      <p className='Title'>{ title }</p>
      <p className='Price'>${ price }</p>
      <p className='StarRating'>{ <Rating rate={rating} /> }</p>
      <div className='imageHolder'>
        <img src={imageURL} alt=''/>
        <br/>
        <br/>
        <button onClick={()=>addToCard(props)}>Add to Cart</button>
      </div>
    </div>
  )
}

export default Card;