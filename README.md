# the neon pyramid
A proof-of-concept online-order app for a fictional cyberpunk-themed restaurant 

### Project Description
> General App Idea/Purpose<br />
> This is an app designed to order food online from The Neon Pyramid, a fictional cyberpunk restaurant serving pan-Eurasian fusion cuisine. 
#### Models<br />

##### User: <br />
>  username = CharField(unique = True) <br />
>  email = CharField(unique = True) <br />
>  phone_num = CharField(unique = True) <br />
>  address = CharField(unique = True) <br />
>  password = CharField(unique = True) <br />
>  paymentInfo = { <br />
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ccNum = CharField() <br />
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ccExp = DateTimeField([formats='%Y-%m-%d']) <br />
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ccSecCode = CharField() <br />
}  <br />

##### Order: <br />
> created_at = DateTimeField(default = datetime.datetime.now) <br />
> total = FloatField() <br />
> user = [{ForeignKeyField(User, backref='orders')}] <br />

##### Dish: <br />
> title = CharField(unique = True) <br />
> price = FloatField() <br />
> image = CharField(unique = True) <br />
> description = CharField(unique = True) <br />
> category = CharField() <br />
> labels = [CharField()] <br />
> order = [{ForeignKeyField(Order, backref='dishes')}] <br />

### Routes
<ul> User:
   <li> create user: neonpyramid/users/register </li> 
   <li> create login: neonpyramid/users/login </li> 
   <li> get logout: neonpyramid/users/logout </li> 
</ul>

<ul> Menu:
   <li> get index: neonpyramid/menu/ </li> 
   <li> get show: neonpyramid/menu/<id> </li>  
</ul>

<ul> Order:
   <li> get index: neonpyramid/order/ </li> 
   <li> create push dish to order: neonpyramid/order/<id> </li>
   <li> destroy splice dish from order: neonpyramid/order/<id> </li>
   <li> create checkout/payment: neonpyramid/order/checkout/<id> </li>
   <li> destroy order: neonpyramid/order/<id> </li>
   <li> show checkout/payment completed: neonpyramid/order/checkout/<id> </li>  
</ul>

### Wireframes
![menu@1x](https://media.git.generalassemb.ly/user/36406/files/04cad700-4cb0-11ec-95b7-9580e57fa13c)
![show@1x](https://media.git.generalassemb.ly/user/36406/files/05fc0400-4cb0-11ec-8b28-d937c4d150dc)
![pay form@1x](https://media.git.generalassemb.ly/user/36406/files/098f8b00-4cb0-11ec-851d-2fd982200746)

### User Stories
<ul>
  <li> As a customer, I want to securely register and login to this app, so that my order history is documented. </li>
  <li> As a customer, I want to see a menu displayed with pictures, prices and descriptions of dishes. </li>
  <li> As a customer, I want to be able to add dishes to an order cart and see the subtotalled price change as I add more dishes.</li>
  <li> As a customer, I want to be able to pay for my order online and have it delivered to my address. </li>
</ul>

#### MVP Goals
<ul>
  <li> Fullstack CRUD application using React (frontend) and Flask (backend)</li>
  <li> Ability to add dishes to an order cart and see prices dynamically totaled</li>
  <li> Be able to add payment info to complete orders online </li>
  <li> Professionally stylized </li>
</ul>


#### Stretch Goals

<ul>
  <li> Animations on certain responses </li>
  <li> Custom Logo </li>
  <li> API connectivity, i.e., order tracking via Google Maps, payments made through PayPal, Square, etc.</li>
  <li> Web accessibility for differently-abled customers.  </li>
  <li> Add-ons for each menu item  </li>
  
</ul>

