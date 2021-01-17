#_*_conding:utf-8_*_
#@Time    :2019/11/2317:34
#@Author  :xiaodong.wu
#@Email   :2586089125@qq.com


"""
requet请求的结构：1. 请求首行：就是访问某个网站的地址（请求方法+url,get http://www.baidu.com?id=10000）
                2.请求头(消息头):请求的内容告诉服务器我的要求，主要包括 Accept:可接受的数据类型
                                                       User_Agent:客户端的类型（客户端的名称，版本等信息）
                                                       Content_Type:传给服务器的数据类型
                3.请求体：用来传参数（GET请求的请求体中没有数据）
                        请求体的数据类型：x-www-form表单
                                      json

request请求方法：get(从服务器中查询参数)，post(新增数据)，put(对服务器中已有数据进行修改)，delete(删除已经有的数据)

响应状态：3xx:重定向（302如你访问的时这个页面，但是返回给你的时另外一个页面）

        4xx:客户端错误
        401：没权限访问
        403：禁止访问
        404：未找到资源

        5xx:服务器错误
        500：服务器内部错误

        2xx:代表成功信息
        200：访问某个站点成功

json结构:对象结构：{
                  ”key1“:"value1",
                  ”key2“:"value2",
                }
                或者
                {
                  {
                    ”key1“:"value1",

                    },
                  {
                    ”key2“:"value2",
                    }
                }
        数组结构:
                [
                  {
                  ”key1“:"value1",
                  ”key2“:"value2",
                  }
                ]
json注意事项：
            1.json格式的数据在Python中以字符串的形式呈现
            2.json中空值为null
            3.json中除数字外，key和value都为字符串且用双引号括起来

session认证：是一种传统的认证机制，session是一个对象，存储客户端会话所需要的属性等信息。
认证过程：客户端向服务器发起登陆请求时，服务器接收到请求时会为每一个session对象分配一个唯一的sessionid
        并通过set_cookie响应给客户端，客户端将sessionid保存到cookie中，用户下一次向服务器发起请求时
        携带cookie中的sessionid给服务器进行验证

token认证：
        客户端输入信息第一次向服务器发送请求时，服务端会生成一个token返回给客户端（浏览器），客户端保存到本地存储
        或会话存储中，用户再次发起请求时会携带token,服务器会对token进行认证（第一次请求产生的token，换一台电脑
        携带上第一次的token也可以进行访问，token具有时效性）


session认证和token认证的区别？
        1.session认证一般用于前端而token认证一般用于后端
        2.token认证服务器不再将token信息保存到服务器或内存中，session会保存
        3.token比起session认证更能减少服务器压力的鉴权机制

"""