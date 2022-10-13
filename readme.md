# Chat Room
A project for learning something.


## Function
- As a visitor, you can choose you initial avatar with a single click.

## FONT-END
vue+ 3.0

## BACK-END
python - flask

## DATABASE

### user

| username | UUID | password | register time | logo |bio | permission |
| -------- | ---- | -------- | ------------- | --- | ---------- |
| testuser | 78787 | first666 | 2022.10.13-21:36 | 78787.jpg |test | 0 |

### roomlist
| roomid | roomname | roombio | portrait | createtime | roomtype | 
| ------ | -------- | ------  | -------- | ---------- | -------- |
| room666666 | testroom | a basic room for test | room666666.jpg | 2022.10.11 - 12:00 | test |

### roommsg
| username | msgcontent | msgtime | msgtype | 
| -------- | ---------- | ------  | ------- | 
| test | hihihi | 2022.10.11 - 12:00 | string |