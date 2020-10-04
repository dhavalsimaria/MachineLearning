

## fallback
- utter_default

## greeting path 1
* greet{"PERSON":"Will"}
  - slot{"PERSON": "Will"}
  - utter_greet

## fine path 1
* fine_normal
  - utter_help

## fine path 2
* fine_ask
  - utter_reply

## thanks path 1
* thanks
  - utter_anything_else

## happy path
* greet{"PERSON":"Will"}
  - slot{"PERSON": "Will"}
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## check balance
* check_balance
  - utter_check_balance

## deposite money
* deposite_money
  - utter_deposite_money

## request cheque book
* request_cheque_book
  - utter_request_cheque_book

## transfer money
* transfer_money
  - utter_transfer_money

## withdraw money
* withdraw_money
  - utter_withdraw_money

