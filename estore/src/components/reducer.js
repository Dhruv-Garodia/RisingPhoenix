export const initialState = {
  cartList:[],
  productList:[{
    title: 'Cisco UCS C220 M3 UCSC-PSU-450W Server 450W.',
    prod_id : '0321732944' ,
    price: '200.57',
    rating: '4',
    imageURL: 'https://www.elecok.com/media/catalog/product/cache/1/image/350x/beebc73da1003953a49a7039599be438/default_psu.jpg'
  },
  {
    title: 'Cisco UCS C220 M3 Server DPS-450AB-1 450W',
    prod_id : '0439806341' ,
    price: '200.96',
    rating: '4',
    imageURL: 'https://www.elecok.com/media/catalog/product/cache/1/image/350x/beebc73da1003953a49a7039599be438/default_psu.jpg'
  },
  {
    title: ' CISCO 34-1977-03 A0 48V0.38A PSA18U-480C',
    prod_id : '0511189877' ,
    price: '105.56',
    rating: '4',
    imageURL: 'https://www.elecok.com/media/catalog/product/cache/1/image/350x/beebc73da1003953a49a7039599be438/ac-adapter.jpeg'
  },
  {
    title: 'Cisco RV260W VPN Router | 8 Gigabit Ethernet (GbE) Ports | Wireless-AC VPN Firewall | Limited Lifetime Protection (RV260W-I-K9-IN).',
    prod_id : '0528881469' ,
    price: '409.00',
    rating: '4',
    imageURL: 'https://m.media-amazon.com/images/I/71xqDouhv7L._SX679_.jpg'
  },
  {
    title: 'Portable Cisco Firewall.',
    prod_id : '0594002320' ,
    price: '90.00',
    rating: '4',
    imageURL: 'https://tiimg.tistatic.com/fp/1/005/685/portable-cisco-firewall-075.jpg'
  },
  {
    title: 'Cisco CISCO ws-c3750G-48PS Fan',
    prod_id : '0594012015' ,
    price: '110.00',
    rating: '4',
    imageURL: 'https://www.elecok.com/media/catalog/product/cache/1/image/350x/beebc73da1003953a49a7039599be438/fan_350.jpg'
  },
  {
    title: 'Cisco SF350-24 Managed Switch | 24 10/100 Ports | 4 Gigabit Ethernet (GbE) Combo SFP.',
    prod_id : '0594451647' ,
    price: '400.00',
    rating: '4',
    imageURL: 'https://encrypted-tbn1.gstatic.com/shopping?q=tbn:ANd9GcTqDdYLz9LkFsIMs-F2sMDVHZfTOPVpGUNAYHELl4f6aOiMcqVyyOPGI_Iz3bu1w95kpnveH6FVbaEaSPUJH48QKpt1irCF1AAjMkahZn7d'
  },
  {
    title: 'ISR4331-K9 Cisco 4331 Router.',
    prod_id : '0594477670' ,
    price: '1500.00',
    rating: '4',
    imageURL: 'https://encrypted-tbn3.gstatic.com/shopping?q=tbn:ANd9GcSRNGDMgUpkcTYDRVh7JOqDH6wwzvtVWlhryykT80tEvT4hqnuj5iRs9KyI38TqhTuMHrzgoARLrSyS7MEQD6_s3JlVn0JQDKaQRV1d-qtR5o6UjUNrnF4f'
  },
  {
    title: 'Cisco Business CBS110 8 Port Desktop Unmanaged Switch, Gigabit Ethernet Technology, 10/100/1000Base-T Network, Layer 2 Support, Rack Mountable, White | CBS110-8T-D.',
    prod_id : '0594481813' ,
    price: '69.00',
    rating: '4',
    imageURL: 'https://microless.com/cdn/products/ff855a3c5a7d1b4c6921272ec2fcb877-hi.jpg'
  }]
};

export const reducer = (state, action) => {
  switch (action.type) {
    case 'ADD_TO_CART':
      return { 
        ...state, 
        cartList:[...state.cartList, action.payload]
      };
    case 'REMOVE_FROM_CART':
      return { 
        ...state, 
        cartList: state.cartList.filter(item => item.id !== action.payload)
      };
    default:
      return state;
  }
}