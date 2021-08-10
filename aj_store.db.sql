--- 10-08-2021 13:34:13
--- aj_store.db
SELECT * FROM user1;

--- 10-08-2021 13:36:39
--- aj_store.db
DELETE FROM user1 WHERE user_id=2; SELECT * FROM user1;

--- 10-08-2021 13:37:22
--- aj_store.db
UPDATE user1 SET 
  user_id='3',
  first_name='Abdul-Malik',
  last_name='Mohamed',
  username='amm',
  email='abdulmalikmohamed360@gmail.com',
  phone='0725658458',
  password='lollipops'
 WHERE user_id=3; SELECT * FROM user1;

--- 10-08-2021 13:37:31
--- aj_store.db
DELETE FROM user1 WHERE user_id=10; SELECT * FROM user1;

--- 10-08-2021 13:37:38
--- aj_store.db
DELETE FROM user1 WHERE user_id=4; SELECT * FROM user1;

--- 10-08-2021 13:37:43
--- aj_store.db
DELETE FROM user1 WHERE user_id=6; SELECT * FROM user1;

--- 10-08-2021 13:37:47
--- aj_store.db
DELETE FROM user1 WHERE user_id=5; SELECT * FROM user1;

--- 10-08-2021 13:37:50
--- aj_store.db
DELETE FROM user1 WHERE user_id=7; SELECT * FROM user1;

--- 10-08-2021 13:37:53
--- aj_store.db
DELETE FROM user1 WHERE user_id=8; SELECT * FROM user1;

--- 10-08-2021 13:38:25
--- aj_store.db
UPDATE user1 SET 
  user_id='1',
  first_name='Aaliyah',
  last_name='Jardien',
  username='aj',
  email='aaliyahjar13gmail.com',
  phone='0679288043',
  password='icecream
'
 WHERE user_id=1; SELECT * FROM user1;

--- 10-08-2021 13:38:36
--- aj_store.db
UPDATE user1 SET 
  user_id='9',
  first_name='Gary',
  last_name='Africa',
  username='ga',
  email='gafrica851@gmail.com',
  phone='0798022267',
  password='milkshakes'
 WHERE user_id=9; SELECT * FROM user1;

--- 10-08-2021 13:38:55
--- aj_store.db
UPDATE user1 SET 
  user_id='1',
  first_name='Aaliyah',
  last_name='Jardien',
  username='aj',
  email='aaliyahjar13gmail.com',
  phone='0679288043',
  password='icecream
'
 WHERE user_id=1; SELECT * FROM user1;

--- 10-08-2021 13:39:06
--- aj_store.db
UPDATE user1 SET 
  user_id='2',
  first_name='Abdul-Malik',
  last_name='Mohamed',
  username='amm',
  email='abdulmalikmohamed360@gmail.com',
  phone='0725658458',
  password='lollipops'
 WHERE user_id=3; SELECT * FROM user1;

--- 10-08-2021 13:39:33
--- aj_store.db
UPDATE user1 SET 
  user_id='3',
  first_name='Gary',
  last_name='Africa',
  username='ga',
  email='gafrica851@gmail.com',
  phone='0798022267',
  password='milkshakes'
 WHERE user_id=9; SELECT * FROM user1;

--- 10-08-2021 13:42:35
--- aj_store.db
INSERT INTO user1 (user_id,first_name,last_name,username,email,phone,password) VALUES (
  '4',
  'Zaid',
  'Flandorp',
  'zf',
  'zaidflandorp4@gmail.com',
  '0740184296',
  'candyfloss'
); SELECT * FROM user1;

--- 10-08-2021 13:44:16
--- aj_store.db
INSERT INTO user1 (user_id,first_name,last_name,username,email,phone,password) VALUES (
  '5',
  'Ayyoob',
  'Slamdien',
  'as',
  'aslamdien90@gmail.com',
  '0614170272',
  'cupcakes'
); SELECT * FROM user1;

--- 10-08-2021 13:46:43
--- aj_store.db
INSERT INTO user1 (user_id,first_name,last_name,username,email,phone,password) VALUES (
  '6',
  'Uthmaan',
  'Breda',
  'ub',
  'uthmaanbreda@gmail.com',
  '0794637741',
  'sweets'
); SELECT * FROM user1;

--- 10-08-2021 13:49:27
--- aj_store.db
SELECT * FROM user1;

--- 10-08-2021 13:49:29
--- aj_store.db
SELECT * FROM user1;

--- 10-08-2021 13:54:05
--- aj_store.db
SELECT * FROM user1;

--- 10-08-2021 13:54:08
--- aj_store.db
SELECT * FROM user;

--- 10-08-2021 13:54:25
--- aj_store.db
DELETE FROM user;

--- 10-08-2021 13:54:31
--- aj_store.db
DROP TABLE user;

--- 10-08-2021 13:54:54
--- aj_store.db
SELECT * FROM item;

--- 10-08-2021 13:58:59
--- aj_store.db
INSERT INTO item (id,item_name,description,item_price,item_barcode) VALUES (
  '1',
  'Sunflower seeds',
  'seeds',
  'R15',
  '12345'
); SELECT * FROM item;

--- 10-08-2021 14:02:22
--- aj_store.db
INSERT INTO item (id,item_name,description,item_price,item_barcode) VALUES (
  '2',
  'Gardening gloves ',
  'Kids Dinosaur Gardening Gloves',
  'R25',
  '12354'
); SELECT * FROM item;

--- 10-08-2021 14:03:17
--- aj_store.db
UPDATE item SET 
  id='1',
  item_name='Plant Seeds',
  description='Sunflower Seeds',
  item_price='R15',
  item_barcode='12345'
 WHERE id=1; SELECT * FROM item;

--- 10-08-2021 14:04:46
--- aj_store.db
INSERT INTO item (id,item_name,description,item_price,item_barcode) VALUES (
  '3',
  'Watering Can',
  'Blue Plastic Watering Can',
  'R50',
  '12543'
); SELECT * FROM item;

--- 10-08-2021 14:05:35
--- aj_store.db
INSERT INTO item (id,item_name,description,item_price,item_barcode) VALUES (
  '4',
  'Soil',
  'Potting Soil',
  'R70',
  '15432'
); SELECT * FROM item;

--- 10-08-2021 14:06:54
--- aj_store.db
INSERT INTO item (id,item_name,description,item_price,item_barcode) VALUES (
  '5',
  'Spade',
  'Green Spade',
  'R90',
  '54321'
); SELECT * FROM item;

--- 10-08-2021 14:09:43
--- aj_store.db
INSERT INTO item (id,item_name,description,item_price,item_barcode) VALUES (
  '6',
  'Sun Hat',
  'Green Sun Hat',
  'R85',
  '43215'
); SELECT * FROM item;

--- 10-08-2021 14:10:56
--- aj_store.db
SELECT * FROM item;

