# punto_de_venta_mtg
Punto de venta en línea para cartas de mtg

# RESTful Structure


||__GET__|__POST__|__PUT__|__DELETE__|
|---|----|----|----|----|
|/api/cards/|Show all cards|Add Card|Update all cards| N/A|
|/api/cards/\<pk\>|N/A|N/A|Update card|Delete Card|
|/api/cart/|Show cards in cart|Add card to cart|Update cards in cart|Empty Cart|
|/api/cart/\<pk\>|Show cards|N/A|Update card \<pk\> in cart|Remove \<pk\> from cart|


# Cards json structure
```
{
    "name": "Plains",
    "price": 0.05,
    "quantity": 2,
    "types": "Basic Land - Plains",
    "set": "DMU",
    "collector_number": 262,
    "condition": "NM",
    "finish": False,
}
``` 