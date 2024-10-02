class Template(object):
    
    def sendMe(self, mid, displayName, picture, cover, status):
        dataProfile = [
            {
                "type": "bubble",
                "size": "kilo",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": cover,
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "aspectRatio": "2:3",
                                    "action": {
                                        "type": "uri",
                                        "uri": "https://line.me/R/nv/profilePopup/mid=" + str(mid)
                                    }
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "image",
                                            "url": picture,
                                            "aspectMode": "cover",
                                            "action": {
                                                "type": "uri",
                                                "uri": picture
                                            }
                                        }
                                    ],
                                    "position": "absolute",
                                    "offsetBottom": "130px",
                                    "offsetStart": "95px",
                                    "cornerRadius": "50px",
                                    "width": "70px",
                                    "height": "70px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": displayName,
                                            "weight": "bold",
                                            "color": "#F6F6F6"
                                        }
                                    ],
                                    "position": "absolute",
                                    "offsetBottom": "107px",
                                    "offsetStart": "75px",
                                    "width": "120px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": status,
                                            "color": "#F6F6F6",
                                            "size": "xxs"
                                        }
                                    ],
                                    "position": "absolute",
                                    "offsetBottom": "90px",
                                    "offsetStart": "85px",
                                    "width": "90px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "image",
                                            "url": "https://i.ibb.co/jTzRBgn/20201216-141953.png",
                                            "aspectRatio": "640:126",
                                            "size": "full",
                                            "offsetStart": "12px"
                                        },
                                        {
                                            "type": "image",
                                            "url": "https://i.ibb.co/njtCjwx/20201216-141922.png",
                                            "aspectRatio": "1280:151",
                                            "size": "240px"
                                        }
                                    ],
                                    "position": "absolute",
                                    "offsetBottom": "0px",
                                    "offsetEnd": "10px",
                                    "spacing": "md"
                                }
                            ]
                        }
                    ],
                    "paddingAll": "0px"
                }
            }
        ]
        return dataProfile
    
    def smallTemp(self, displayName, picture, text, text2):
        dataProfile = {
            "type": "flex",
            "altText": "{} is reading".format(displayName),
            "contents": {
                "type": "bubble",
                "size": "micro",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "image",
                                    "url": picture,
                                    "size": "full",
                                    "aspectMode": "cover",
                                    "gravity": "center",
                                    "flex": 1
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": str(text2),
                                            "size": "xxs",
                                            "color": "#ffffff",
                                            "align": "center",
                                            "gravity": "center",
                                            "position": "absolute",
                                            "offsetEnd": "2.5px",
                                            "offsetBottom": "1px",
                                            "offsetStart": "1px"
                                        }
                                    ],
                                    "backgroundColor": "#EC3D44",
                                    "paddingAll": "2px",
                                    "paddingStart": "4px",
                                    "paddingEnd": "4px",
                                    "flex": 0,
                                    "position": "absolute",
                                    "offsetStart": "7px",
                                    "offsetTop": "7px",
                                    "cornerRadius": "100px",
                                    "width": "40px",
                                    "height": "10px",
                                    "paddingBottom": "14px"
                                }
                            ]
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "text",
                                            "text": str(displayName),
                                            "color": "#81ff00",
                                            "size": "xxs",
                                            "align": "center",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "separator",
                                            "color": "#81ff00"
                                        },
                                        {
                                            "type": "text",
                                            "text": str(text),
                                            "color": "#81ff00",
                                            "size": "xxs",
                                            "align": "center",
                                            "weight": "bold"
                                        }
                                    ]
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "0px",
                            "backgroundColor": "#5b5b5bcc",
                            "cornerRadius": "5px",
                            "width": "160px"
                        }
                    ],
                    "paddingAll": "0px"
                }
            }
        }
        return dataProfile
    
    def instagram(self, text, tempStyle, pictGroup, name):
        if tempStyle == "dark":
            upPict = "https://i.ibb.co/710XS08/c03c907e1275.jpg"
            upRatio = "1280:176"
            downPict = "https://i.ibb.co/0Xv9VZY/Sozibot.jpg"
            downRatio = "1280:186"
            backColor = "#000000"
            nameColor = "#FFFFFF"
            bubbleColor = "#262626"
        else:
            upPict = "https://i.ibb.co/8bStpvn/90eac7aa2519.jpg"
            upRatio = "1280:175"
            downPict = "https://i.ibb.co/JpGNgCg/Sozi.jpg"
            downRatio = "1280:165"
            backColor = "#FFFFFF"
            nameColor = "#000000"
            bubbleColor = "#EFEFEF"
        dataProfile = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": upPict,
                        "size": "full",
                        "aspectRatio": upRatio,
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/nv/chat"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": pictGroup,
                                "size": "full",
                                "aspectMode": "cover",
                                "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/R/ti/p/~arshleo"
                                }
                            }
                        ],
                        "position": "absolute",
                        "width": "25px",
                        "height": "25px",
                        "cornerRadius": "100px",
                        "offsetStart": "42px",
                        "offsetTop": "8px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": name,
                                "size": "sm",
                                "color": nameColor,
                                "weight": "bold",
                                "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/R/ti/p/~arshleo"
                                }
                            }
                        ],
                        "backgroundColor": "#ffffff00",
                        "position": "absolute",
                        "offsetTop": "12px",
                        "offsetStart": "85px",
                        "width": "110px"
                    },
                    {
                        "type": "separator",
                        "color": nameColor
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": backColor
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": text,
                                        "color": nameColor,
                                        "wrap": True,
                                        "size": "xs"
                                    }
                                ],
                                "backgroundColor": bubbleColor,
                                "paddingAll": "5px",
                                "cornerRadius": "14px",
                                "width": "220px"
                            }
                        ],
                        "alignItems": "flex-end"
                    }
                ],
                "backgroundColor": backColor,
                "spacing": "sm",
                "paddingAll": "4px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": downPict,
                        "size": "full",
                        "aspectRatio": downRatio,
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/ti/p/~arshleo"
                        }
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": backColor
            }
        }
        return dataProfile
    
    def telegram(self, text, tempStyle, pictGroup, name, myName, cmd, msgId, hours, minutes):
        if tempStyle == "dark":
            upPict = "https://i.ibb.co/k2Q9t6B/7b76ff04892c.jpg"
            upColor = "#1C1C1D"
            upRatio = "1280:157"
            downPict = "https://i.ibb.co/DtC860m/Sozileo.jpg"
            downColor = "#1C1C1D"
            downRatio = "1280:157"
            backColor = "#2C2C2E"
            todayColor = "#202020"
            todayColor2 = "#666666"
            bubbleColor = "#B3B3B3"
            textColor = "#000000"
            textColor2 = "#000000"
            textColor3 = "#FFFFFF"
        else:
            upPict = "https://i.ibb.co/ZVKRH4z/cd89c17ce17a.jpg"
            upColor = "#F6F6F6"
            upRatio = "1280:158"
            downPict = "https://i.ibb.co/JpGNgCg/Sozi.jpg"
            downColor = "#F6F6F6"
            downRatio = "1280:165"
            backColor = "#D2D2D2"
            todayColor = "#00000033"
            todayColor2 = "#FFFFFF"
            bubbleColor = "#3774B1"
            textColor = "#FFFFFF"
            textColor2 = "#7ECEFF"
            textColor3 = "#000000"
        dataProfile = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "image",
                        "url": upPict,
                        "size": "full",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/nv/chat"
                        },
                        "aspectRatio": upRatio
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": pictGroup,
                                "size": "full",
                                "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/R/ti/p/~arshleo"
                                },
                                "aspectMode": "cover"
                            }
                        ],
                        "position": "absolute",
                        "width": "30px",
                        "height": "30px",
                        "cornerRadius": "100px",
                        "offsetEnd": "5px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": name,
                                "size": "sm",
                                "color": textColor3,
                                "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/R/ti/p/~arshleo"
                                },
                                "weight": "bold",
                                "align": "center"
                            }
                        ],
                        "backgroundColor": "#ffffff00",
                        "position": "absolute",
                        "offsetTop": "10px",
                        "offsetStart": "80px",
                        "width": "150px"
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": upColor,
                "alignItems": "center"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "T O D A Y",
                                        "size": "7px",
                                        "weight": "bold",
                                        "color": todayColor2
                                    }
                                ],
                                "backgroundColor": todayColor,
                                "cornerRadius": "50px",
                                "paddingAll": "4px"
                            }
                        ],
                        "alignItems": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [],
                                                "width": "3px",
                                                "backgroundColor": textColor2,
                                                "borderWidth": "1px",
                                                "action": {
                                                    "type": "uri",
                                                    "uri": msgId
                                                }
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": myName,
                                                        "size": "xs",
                                                        "weight": "bold",
                                                        "color": textColor2,
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": msgId
                                                        }
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": cmd,
                                                        "size": "xxs",
                                                        "color": textColor,
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": msgId
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        "spacing": "md",
                                        "paddingTop": "5px",
                                        "paddingStart": "10px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": text,
                                                "color": textColor,
                                                "wrap": True,
                                                "size": "xs"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": "{}:{}".format(hours, minutes),
                                                        "color": "#ffffff",
                                                        "size": "9px"
                                                    }
                                                ],
                                                "alignItems": "flex-end",
                                                "offsetEnd": "15px"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": "https://i.ibb.co/5kXzN4W/1602905613052.png",
                                                        "aspectRatio": "329:241",
                                                        "size": "20px"
                                                    }
                                                ],
                                                "position": "absolute",
                                                "offsetBottom": "5px",
                                                "offsetEnd": "1px"
                                            }
                                        ],
                                        "paddingAll": "5px"
                                    }
                                ],
                                "backgroundColor": bubbleColor,
                                "cornerRadius": "14px",
                                "width": "220px"
                            }
                        ],
                        "alignItems": "flex-end"
                    }
                ],
                "backgroundColor": backColor,
                "spacing": "sm",
                "paddingAll": "4px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": downPict,
                        "size": "full",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/ti/p/~arshleo"
                        },
                        "aspectRatio": downRatio
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": downColor
            }
        }
        return dataProfile
    
    def whatsapp(self, text, tempStyle, pictGroup, name, hours, minutes):
        if tempStyle == "dark":
            upPict = "https://i.ibb.co/Xp63jpp/ffa169e85a87.jpg"
            upColor = "#171717"
            upRatio = "1280:156"
            downPict = "https://i.ibb.co/pvby87C/Sozibot.jpg"
            downColor = "#171717"
            downRatio = "3264:398"
            todayColor = "#202020"
            todayColor2 = "#666666"
            backColor = "#2C2C2E"
            bubbleColor = "#056362"
            textColor = "#FFFFFF"
            textColor2 = "#419192"
        else:
            upPict = "https://i.ibb.co/R6QTGm3/cf32a5c3e9ce.jpg"
            upColor = "#F6F6F6"
            upRatio = "1280:157"
            downPict = "https://i.ibb.co/Y063bQN/Sozi.jpg"
            downColor = "#F6F6F6"
            downRatio = "3264:398"
            todayColor = "#8BACD973"
            todayColor2 = "#FFFFFF"
            backColor = "#D2D2D2"
            bubbleColor = "#DAF6C5"
            textColor = "#000000"
            textColor2 = "#484848"
        dataProfile = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": upPict,
                        "size": "full",
                        "aspectRatio": upRatio,
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/nv/chat"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": pictGroup,
                                "size": "full",
                                "aspectMode": "cover",
                                "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/R/ti/p/~arshleo"
                                }
                            }
                        ],
                        "position": "absolute",
                        "width": "30px",
                        "height": "30px",
                        "cornerRadius": "100px",
                        "offsetStart": "30px",
                        "offsetTop": "4px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": name, 
                                "size": "sm",
                                "color": textColor,
                                "weight": "bold",
                                "action": {
                                    "type": "uri",
                                    "uri": "https://line.me/R/ti/p/~arshleo"
                                }
                            }
                        ],
                        "backgroundColor": "#ffffff00",
                        "position": "absolute",
                        "offsetTop": "10px",
                        "offsetStart": "70px",
                        "width": "110px"
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": upColor
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "T O D A Y",
                                        "color": todayColor2,
                                        "size": "7px",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": todayColor,
                                "cornerRadius": "50px",
                                "paddingAll": "4px",
                                "alignItems": "center"
                            }
                        ],
                        "alignItems": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": text,
                                        "color": textColor,
                                        "wrap": True,
                                        "size": "xs"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "{}.{}".format(hours, minutes),
                                                "color": textColor2,
                                                "size": "9px"
                                            }
                                        ],
                                        "alignItems": "flex-end",
                                        "offsetEnd": "15px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "image",
                                                "url": "https://i.ibb.co/5kXzN4W/1602905613052.png",
                                                "aspectRatio": "329:241",
                                                "size": "20px"
                                            }
                                        ],
                                        "position": "absolute",
                                        "offsetEnd": "1px",
                                        "offsetBottom": "5px"
                                    }
                                ],
                                "backgroundColor": bubbleColor,
                                "paddingAll": "5px",
                                "cornerRadius": "14px",
                                "width": "220px"
                            }
                        ],
                        "alignItems": "flex-end"
                    }
                ],
                "backgroundColor": backColor,
                "spacing": "sm",
                "paddingAll": "4px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": downPict,
                        "size": "full",
                        "aspectRatio": downRatio,
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/ti/p/~arshleo"
                        }
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": downColor
            }
        }
        return dataProfile

    def line(self, text, tempStyle, pictGroup, pictReply, name, nameReply, cmd, msgId, hours, minutes):
        if tempStyle == "dark":
            upPict = "https://i.ibb.co/QfCbC8J/d7dda6cc2428.jpg"
            upColor = "#121212"
            upRatio = "1280:157"
            downPict = "https://i.ibb.co/8gVhmWy/sozi.jpg"
            downColor = "#121212"
            downRatio = "1280:170"
            backColor = "#121212"
            todayColor = "#202020"
            todayColor2 = "#666666"
            bubbleColor = "#595959"
            textColor = "#FFFFFF"
            textColor2 = "#4F4F4F"
            textColor3 = "#909090"
        else:
            upPict = "https://i.ibb.co/xD1P3CX/419907cb3790.jpg"
            upColor = "#8BACD9"
            upRatio = "1280:174"
            downPict = "https://i.ibb.co/DMBzrbw/sozi.jpg"
            downColor = "#FFFFFF"
            downRatio = "1280:165"
            backColor = "#8BACD9"
            todayColor = "#00000033"
            todayColor2 = "#FFFFFF"
            bubbleColor = "#9DE693"
            textColor = "#000000"
            textColor2 = "#000000"
            textColor3 = "#484848"
        dataProfile = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": upPict,
                        "size": "full",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/nv/chat"
                        },
                        "aspectRatio": upRatio
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": name,
                                "size": "sm",
                                "color": textColor,
                                "weight": "bold"
                            }
                        ],
                        "backgroundColor": "#00000000",
                        "position": "absolute",
                        "offsetTop": "10px",
                        "offsetStart": "30px",
                        "width": "150px"
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": upColor
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "T O D A Y",
                                        "color": todayColor2,
                                        "size": "7px",
                                        "weight": "bold"
                                    }
                                ],
                                "backgroundColor": todayColor,
                                "cornerRadius": "50px",
                                "paddingAll": "4px",
                                "alignItems": "center"
                            }
                        ],
                        "alignItems": "center"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": "{}:{}".format(hours, minutes),
                                "align": "end",
                                "offsetEnd": "5px",
                                "size": "xxs",
                                "color": textColor2
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": pictReply,
                                                        "size": "full",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": msgId
                                                        },
                                                        "aspectMode": "cover"
                                                    }
                                                ],
                                                "width": "20px",
                                                "height": "20px",
                                                "cornerRadius": "100px"
                                            },
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "text",
                                                        "text": nameReply,
                                                        "size": "xs",
                                                        "weight": "bold",
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": msgId
                                                        },
                                                        "color": textColor
                                                    },
                                                    {
                                                        "type": "text",
                                                        "text": cmd,
                                                        "size": "xxs",
                                                        "color": textColor3,
                                                        "action": {
                                                            "type": "uri",
                                                            "uri": msgId
                                                        }
                                                    }
                                                ]
                                            }
                                        ],
                                        "spacing": "md",
                                        "alignItems": "center",
                                        "paddingAll": "5px"
                                    },
                                    {
                                        "type": "separator",
                                        "color": "#484848"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": text,
                                                "color": textColor,
                                                "wrap": True,
                                                "size": "xs"
                                            }
                                        ],
                                        "paddingAll": "5px"
                                    }
                                ],
                                "backgroundColor": bubbleColor,
                                "cornerRadius": "17px",
                                "width": "220px"
                            }
                        ],
                        "alignItems": "flex-end"
                    }
                ],
                "backgroundColor": backColor,
                "spacing": "sm",
                "paddingAll": "4px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": downPict,
                        "size": "full",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/ti/p/~arshleo"
                        },
                        "aspectRatio": downRatio
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": downColor
            }
        }
        return dataProfile
    
    def nhentai(self, title, id, page, uploaded):
        dataProfile = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "NHentai",
                        "weight": "bold",
                        "color": "#F778A1",
                        "size": "xs"
                    },
                    {
                        "type": "text",
                        "text": title,
                        "weight": "bold",
                        "size": "sm",
                        "color": "#FFFFFF"
                    },
                    {
                        "type": "separator",
                        "margin": "sm",
                        "color": "#FFFFFF"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Comic ID",
                                        "size": "sm",
                                        "color": "#FFFFFF",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": id,
                                        "size": "sm",
                                        "color": "#F778A1",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Page",
                                        "size": "sm",
                                        "color": "#FFFFFF",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": page,
                                        "size": "sm",
                                        "color": "#F778A1",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Uploaded",
                                        "size": "sm",
                                        "color": "#FFFFFF",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": uploaded,
                                        "size": "sm",
                                        "color": "#F778A1",
                                        "align": "end"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "separator",
                        "margin": "xxl",
                        "color": "#FFFFFF"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Read Online",
                                "size": "xs",
                                "color": "#C24641",
                                "flex": 0
                            },
                            {
                                "type": "text",
                                "text": "Tap Here!!!",
                                "color": "#C24641",
                                "size": "xs",
                                "align": "end"
                            }
                        ],
                        "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://cin.cin.pw/v/{}".format(id)
                        }
                    }
                ],
                "backgroundColor": "#000000"
            },
            "styles": {
                "footer": {
                    "separator": True
                }
            }
        }
        return dataProfile
    
    def youtube(self, thumbnail, title, mp3, mp4):
        dataProfile = {
            "type": "bubble",
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.ibb.co/zRLy5fM/Pics-Art-07-25-06-52-17.png",
                                "size": "full",
                                "aspectRatio": "80:7.5",
                                "offsetTop": "1.5px"
                            }
                        ],
                        "offsetBottom": "12.5px",
                        "height": "25px"
                    }
                ],
                "backgroundColor": "#424242",
                "height": "25px"
            },
            "hero": {
                "type": "image",
                "url": thumbnail,
                "size": "full",
                "aspectRatio": "9:5.1",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": thumbnail
                }
            },
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://1.bp.blogspot.com/-B4WYl2fhVl8/XDdGAIe3xwI/AAAAAAAAGvA/g86UJjU5iiU63eqK8aCbwCQjodcndmZtQCK4BGAYYCw/s1600/logo%2Byoutube.png",
                                "size": "full",
                                "aspectRatio": "80:65"
                            }
                        ],
                        "width": "60px",
                        "height": "50px",
                        "offsetBottom": "2px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": title,
                                "color": "#FF0000",
                                "size": "xxs",
                                "weight": "bold",
                                "align": "start",
                                "wrap": True,
                                "offsetStart": "5px"
                            }
                        ],
                        "offsetStart": "5px",
                        "height": "50px",
                        "offsetBottom": "2px"
                    }
                ],
                "backgroundColor": "#424242",
                "height": "70px"
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "Audio",
                        "color": "#FF0000",
                        "weight": "bold",
                        "size": "xxs",
                        "align": "center",
                        "offsetBottom": "1px",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/app/1657710460-y83a8lNE?type=text&text={}".format(mp3)
                        }
                    },
                    {
                        "type": "text",
                        "text": "Video",
                        "color": "#FF0000",
                        "weight": "bold",
                        "size": "xxs",
                        "align": "center",
                        "offsetBottom": "1px",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/app/1657710460-y83a8lNE?type=text&text={}".format(mp4)
                        }
                    }
                ],
                "height": "25px",
                "paddingAll": "0px",
                "paddingTop": "5px"
            },
            "styles": {
                "hero": {
                    "separator": True,
                    "separatorColor": "#FF0000"
                },
                "body": {
                    "separator": True,
                    "separatorColor": "#FF0000"
                },
                "footer": {
                    "backgroundColor": "#424242",
                    "separatorColor": "#FF0000",
                    "separator": True
                }
            }
        }
        return dataProfile
    
    def smule(self, cover, artist, command):
        dataProfile = {
            "type": "bubble",
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://cdn.freelogovectors.net/wp-content/uploads/2019/02/smule_logo.png",
                                "size": "full",
                                "aspectRatio": "80:7.5",
                                "offsetTop": "1.5px"
                            }
                        ],
                        "offsetBottom": "12.5px",
                        "height": "25px"
                    }
                ],
                "backgroundColor": "#424242",
                "height": "25px"
            },
            "hero": {
                "type": "image",
                "url": cover,
                "size": "full",
                "aspectRatio": "9:5.1",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": cover
                }
            },
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://images.squarespace-cdn.com/content/v1/5a498ab38a02c76203266964/1558891948231-FAPE8W1C312IZA3CB5LK/ke17ZwdGBToddI8pDm48kDa-iAJ6QNsB7WackDpNdKNZw-zPPgdn4jUwVcJE1ZvWhcwhEtWJXoshNdA9f1qD7TjHkaYfD5WE2gtMQ4su2XqQqr4XHUPgeWykuHk5C_DMSbm74PvoPcGMvWRtr05kyw/Smule_on_Gradient_BG_Small.png",
                                "size": "full",
                                "aspectRatio": "80:65"
                            }
                        ],
                        "width": "60px",
                        "height": "50px",
                        "offsetBottom": "2px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": artist,
                                "color": "#48E667",
                                "size": "xxs",
                                "weight": "bold",
                                "align": "start",
                                "wrap": True,
                                "offsetStart": "5px"
                            }
                        ],
                        "offsetStart": "5px",
                        "height": "50px",
                        "offsetBottom": "2px"
                    }
                ],
                "backgroundColor": "#424242",
                "height": "70px"
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "DOWNLOAD",
                        "color": "#48E667",
                        "weight": "bold",
                        "size": "xxs",
                        "align": "center",
                        "offsetBottom": "1px",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/app/1657710460-y83a8lNE?type=text&text={}".format(command)
                        }
                    }
                ],
                "height": "25px",
                "paddingAll": "0px",
                "paddingTop": "5px"
            },
            "styles": {
                "hero": {
                    "separator": True,
                    "separatorColor": "#48E667"
                },
                "body": {
                    "separator": True,
                    "separatorColor": "#48E667"
                },
                "footer": {
                    "backgroundColor": "#424242",
                    "separatorColor": "#48E667",
                    "separator": True
                }
            }
        }
        return dataProfile

    def github_main(self, username, name, avatar, bio, followers, following, repos, more, tab, color1, color2, color3, dataP):
        dataProfile = {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.ibb.co/T1gDmqd/hlth-github-header.jpg",
                                "aspectRatio": "6:1",
                                "aspectMode": "cover",
                                "size": "full",
                                "align": "center"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "box",
                                                "layout": "vertical",
                                                "contents": [
                                                    {
                                                        "type": "image",
                                                        "url": avatar,
                                                        "aspectRatio": "1:1",
                                                        "aspectMode": "cover",
                                                        "size": "full",
                                                        "align": "center",
                                                        "action": {
                                                            "type": "uri",
                                                            "label": "User",
                                                            "uri": "https://github.com/{}".format(username) 
                                                        }
                                                    }
                                                ],
                                                "width": "42.8px",
                                                "height": "42.8px",
                                                "cornerRadius": "600px"
                                            }
                                        ],
                                        "width": "49px",
                                        "height": "49px",
                                        "cornerRadius": "600px",
                                        "paddingAll": "2px",
                                        "borderWidth": "1px",
                                        "borderColor": "#666666"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": name,
                                                "weight": "bold",
                                                "size": "lg",
                                                "color": "#000000"
                                            },
                                            {
                                                "type": "text",
                                                "text": username,
                                                "size": "xs",
                                                "color": "#666666"
                                            }
                                        ]
                                    }
                                ],
                                "spacing": "md"
                            },
                            {
                                "type": "text",
                                "text": bio,
                                "wrap": True,
                                "size": "xxs",
                                "color": "#666666",
                                "style": "italic",
                                "offsetTop": "5px"
                            }
                        ],
                        "paddingAll": "20px"
                    },
                    {
                        "type": "separator",
                        "color": "#666666"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "action": {
                                    "type": "uri",
                                    "label": "Followers",
                                    "uri": "https://github.com/{}?tab=followers".format(username) 
                                },
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Followers",
                                                "size": "8px",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": followers,
                                                "size": "16px",
                                                "weight": "bold",
                                                "align": "center",
                                                "offsetBottom": "2px"
                                            }
                                        ],
                                        "height": "35px",
                                        "paddingAll": "5px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "backgroundColor": color1,
                                        "height": "5px"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "color": "#666666"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "action": {
                                    "type": "uri",
                                    "label": "Followings",
                                    "uri": "https://github.com/{}?tab=following".format(username) 
                                },
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Following",
                                                "size": "8px",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": following,
                                                "size": "16px",
                                                "weight": "bold",
                                                "align": "center",
                                                "offsetBottom": "2px"
                                            }
                                        ],
                                        "height": "35px",
                                        "paddingAll": "5px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "backgroundColor": color2,
                                        "height": "5px"
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "color": "#666666"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "action": {
                                    "type": "uri",
                                    "label": "Repository",
                                    "uri": "https://github.com/{}?tab=repositories".format(username) 
                                },
                                "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                            {
                                                "type": "text",
                                                "text": "Repository",
                                                "size": "8px",
                                                "align": "center"
                                            },
                                            {
                                                "type": "text",
                                                "text": repos,
                                                "size": "16px",
                                                "weight": "bold",
                                                "align": "center",
                                                "offsetBottom": "2px"
                                            }
                                        ],
                                        "height": "35px",
                                        "paddingAll": "5px"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [],
                                        "backgroundColor": color3,
                                        "height": "5px"
                                    }
                                ]
                            }
                        ],
                        "height": "40px"
                    },
                    {
                        "type": "separator",
                        "color": "#666666"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": dataP,
                        "paddingAll": "10px",
                        "spacing": "sm"
                    }
                ],
                "paddingAll": "0px"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": more,
                        "wrap": True,
                        "align": "center",
                        "size": "xxs",
                        "color": "#666666"
                    }
                ],
                "paddingAll": "5px",
                "action": {
                    "type": "uri",
                    "label": "Followers",
                    "uri": "https://github.com/{}?tab={}".format(username, tab) 
                }
            }
        }
        return dataProfile
    
    def github_followers(self, avatar, login):
        dataProfile = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": avatar,
                            "size": "full",
                            "align": "center",
                            "aspectRatio": "1:1",
                            "aspectMode": "cover"
                        }
                    ],
                    "width": "20px"
                },
                {
                    "type": "text",
                    "text": login,
                    "size": "xxs",
                    "offsetTop": "3px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Follow",
                            "color": "#ffffff",
                            "size": "xxs",
                            "offsetEnd": "10px"
                        }
                    ],
                    "cornerRadius": "5px",
                    "backgroundColor": "#ababab",
                    "alignItems": "flex-end",
                    "width": "60px",
                    "paddingAll": "3px",
                    "action": {
                        "type": "uri",
                        "label": "Profile",
                        "uri": "https://github.com/{}".format(login)
                    }
                }
            ],
            "height": "20px",
            "spacing": "md"
        }
        return dataProfile
    
    def github_following(self, avatar, login):
        dataProfile = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": avatar,
                            "size": "full",
                            "align": "center",
                            "aspectRatio": "1:1",
                            "aspectMode": "cover"
                        }
                    ],
                    "width": "20px"
                },
                {
                    "type": "text",
                    "text": login,
                    "size": "xxs",
                    "offsetTop": "3px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Follow",
                            "color": "#ffffff",
                            "size": "xxs",
                            "offsetEnd": "10px"
                        }
                    ],
                    "cornerRadius": "5px",
                    "backgroundColor": "#ababab",
                    "alignItems": "flex-end",
                    "width": "60px",
                    "paddingAll": "3px",
                    "action": {
                        "type": "uri",
                        "label": "Profile",
                        "uri": "https://github.com/{}".format(login)
                    }
                }
            ],
            "height": "20px",
            "spacing": "md"
        }
        return dataProfile
    
    def github_repos(self, name, url):
        dataProfile = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://i.ibb.co/9nQcB07/kisspng-github-logo-repository-computer-icons-5afa376c51ca94-38716653152634.png",
                            "size": "full",
                            "align": "center",
                            "aspectRatio": "1:1",
                            "aspectMode": "cover"
                        }
                    ],
                    "width": "20px"
                },
                {
                    "type": "text",
                    "text": name,
                    "size": "xxs",
                    "offsetTop": "3px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Open",
                            "color": "#ffffff",
                            "size": "xxs",
                            "offsetEnd": "10px"
                        }
                    ],
                    "cornerRadius": "5px",
                    "backgroundColor": "#ababab",
                    "alignItems": "flex-end",
                    "width": "60px",
                    "paddingAll": "3px",
                    "action": {
                        "type": "uri",
                        "label": "Profile",
                        "uri": url
                    }
                }
            ],
            "height": "20px",
            "spacing": "md"
        }
        return dataProfile
    
    def joox(self, thumbnail, title, command):
        dataProfile = {
            "type": "bubble",
            "size": "kilo",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.ibb.co/3YKkC3c/1607934805184.png",
                                "size": "full",
                                "aspectRatio": "50:7.5",
                                "offsetTop": "1.5px"
                            }
                        ],
                        "offsetBottom": "12.5px",
                        "height": "25px"
                    }
                ],
                "backgroundColor": "#424242",
                "height": "25px"
            },
            "hero": {
                "type": "image",
                "url": thumbnail,
                "size": "full",
                "aspectRatio": "9:5.1",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": thumbnail
                }
            },
            "body": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": "https://i.ibb.co/7YSKsqy/f769eb1f3a33.jpg",
                                "size": "full",
                                "aspectRatio": "80:65"
                            }
                        ],
                        "width": "60px",
                        "height": "50px",
                        "offsetBottom": "2px"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "text",
                                "text": title,
                                "color": "#48E667",
                                "size": "xxs",
                                "weight": "bold",
                                "align": "start",
                                "wrap": True,
                                "offsetStart": "5px"
                            }
                        ],
                        "offsetStart": "5px",
                        "height": "50px",
                        "offsetBottom": "2px"
                    }
                ],
                "backgroundColor": "#424242",
                "height": "70px"
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {
                        "type": "text",
                        "text": "DOWNLOAD",
                        "color": "#48E667",
                        "weight": "bold",
                        "size": "xxs",
                        "align": "center",
                        "offsetBottom": "1px",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/app/1657710460-y83a8lNE?type=text&text={}".format(command)
                        }
                    }
                ],
                "height": "25px",
                "paddingAll": "0px",
                "paddingTop": "5px"
            },
            "styles": {
                "hero": {
                    "separator": True,
                    "separatorColor": "#48E667"
                },
                "body": {
                    "separator": True,
                    "separatorColor": "#48E667"
                },
                "footer": {
                    "backgroundColor": "#424242",
                    "separatorColor": "#48E667",
                    "separator": True
                }
            }
        }
        return dataProfile
    
    def bmkg(self, magnitudo, date, location, koordinat, arahan, image):
        dataProfile = [
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "image",
                            "url": "https://i.ibb.co/sgsZwnQ/ee19dbfa47e8.jpg",
                            "size": "full",
                            "gravity": "center",
                            "aspectRatio": "4:5",
                            "aspectMode": "cover"
                        },
                        {
                            "type": "image",
                            "url": "https://i.ibb.co/sjkxHyW/0c8cd5afec8f.png",
                            "position": "absolute",
                            "aspectMode": "cover",
                            "aspectRatio": "4:5",
                            "offsetTop": "0px",
                            "offsetBottom": "0px",
                            "offsetStart": "0px",
                            "offsetEnd": "0px",
                            "size": "full"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": magnitudo,
                                    "color": "#ffb904",
                                    "size": "4xl",
                                    "weight": "bold",
                                    "align": "center"
                                },
                                {
                                    "type": "text",
                                    "text": "- MAG -",
                                    "color": "#ffffff",
                                    "weight": "bold",
                                    "size": "md",
                                    "align": "center",
                                    "offsetBottom": "5px"
                                }
                            ],
                            "position": "absolute",
                            "offsetBottom": "30px",
                            "backgroundColor": "#212121cc",
                            "offsetStart": "9px",
                            "cornerRadius": "10px",
                            "height": "95px",
                            "width": "85px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "GEMPA",
                                    "color": "#ffffff",
                                    "align": "center",
                                    "size": "xs",
                                    "weight": "bold",
                                    "offsetTop": "-1px",
                                    "offsetEnd": "1px"
                                }
                            ],
                            "position": "absolute",
                            "cornerRadius": "20px",
                            "offsetTop": "11px",
                            "backgroundColor": "#ff0000",
                            "offsetStart": "10px",
                            "height": "17px",
                            "width": "55px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": date,
                                    "weight": "bold",
                                    "color": "#e5e5e5",
                                    "wrap": True,
                                    "size": "xxs"
                                },
                                {
                                    "type": "text",
                                    "color": "#e5e5e5",
                                    "text": location,
                                    "weight": "bold",
                                    "wrap": True,
                                    "size": "xs"
                                },
                                {
                                    "type": "text",
                                    "color": "#e5e5e5",
                                    "text": koordinat,
                                    "weight": "bold",
                                    "wrap": True,
                                    "size": "xxs"
                                },
                                {
                                    "type": "text",
                                    "text": arahan,
                                    "color": "#ffb904",
                                    "wrap": True,
                                    "size": "xxs",
                                    "weight": "bold"
                                }
                            ],
                            "position": "absolute",
                            "width": "188px",
                            "height": "120px",
                            "offsetBottom": "3px",
                            "offsetStart": "100px"
                        }
                    ],
                    "paddingAll": "0px"
                },
                "styles": {
                    "body": {
                        "backgroundColor": "#2e2e2e"
                    }
                }
            },
            {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": image,
                            "size": "full",
                            "aspectMode": "cover",
                            "aspectRatio": "4:5",
                            "action": {
                                "type": "uri",
                                "label": "action",
                                "uri": image
                            }
                        }
                    ]
                }
            }
        ]
        return dataProfile
    
    def old_main_menu(self, picture, name, setkey, url, text=".", text2=".", text3=".", text4=".", text5=".", text6=".", text7=".", text8=".", text9=".", text10="."):
        dataProfile = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://i.ibb.co/2MB7qwT/sozibot.jpg",
                        "aspectRatio": "1.02:1.31",
                        "size": "full",
                        "aspectMode": "cover"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "position": "absolute",
                        "width": "90px",
                        "height": "90px",
                        "offsetStart": "15px",
                        "offsetTop": "15px",
                        "action": {
                            "type": "uri",
                            "uri": "https://line.me/R/ti/p/~arshleo"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "image",
                                "url": picture,
                                "aspectRatio": "1:1",
                                "aspectMode": "cover",
                                "size": "xs",
                                "action": {
                                    "type": "uri",
                                    "label": "action",
                                    "uri": picture
                                }
                            }
                        ],
                        "position": "absolute",
                        "cornerRadius": "100px",
                        "offsetBottom": "31px",
                        "offsetStart": "21px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "position": "absolute",
                        "width": "100px",
                        "height": "30px",
                        "offsetStart": "100px",
                        "action": {
                            "type": "uri",
                            "uri": url
                        },
                        "offsetBottom": "41px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "SETKEY: [ {} ]".format(setkey),
                                "color": "#c3a783",
                                "size": "lg",
                                "weight": "bold",
                                "decoration": "underline"
                            }
                        ],
                        "position": "absolute",
                        "offsetStart": "105px",
                        "offsetTop": "90px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetStart": "50px",
                        "offsetTop": "130px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text2,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetTop": "160px",
                        "offsetStart": "50px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text3,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetTop": "190px",
                        "offsetStart": "50px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text4,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetTop": "220px",
                        "offsetStart": "50px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text5,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetTop": "250px",
                        "offsetStart": "50px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text6,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetStart": "160px",
                        "offsetTop": "130px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text7,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetStart": "160px",
                        "offsetTop": "160px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text8,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetStart": "160px",
                        "offsetTop": "190px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text9,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetStart": "160px",
                        "offsetTop": "220px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": text10,
                                "color": "#c3a783",
                                "size": "sm"
                            }
                        ],
                        "position": "absolute",
                        "offsetStart": "160px",
                        "offsetTop": "250px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": name,
                                "color": "#c3a783",
                                "size": "xxs",
                                "weight": "bold",
                                "align": "center"
                            }
                        ],
                        "position": "absolute",
                        "offsetStart": "97px",
                        "offsetBottom": "48px",
                        "width": "100px"
                    }
                ],
                "paddingAll": "0px"
            },
            "styles": {
                "body": {
                    "backgroundColor": "#02101e"
                }
            }
        }
        return dataProfile
    
    def data_square_temp(self, url, url2):
        dataProfile = {
            "type": "bubble",
            "size": "micro",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": url,
                        "size": "full",
                        "aspectRatio": "3:3.2",
                        "aspectMode": "cover",
                        "action": {
                            "type": "uri",
                            "uri": url2
                        }
                    }
                ],
                "paddingAll": "0px",
                "backgroundColor": "#000000"
            }
        }
        return dataProfile
    
    def main_toggle(self):
        dataProfile = {
            "type": "bubble",
            "size": "kilo",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [],
                "backgroundColor": "#28364E",
                "borderWidth": "3px",
                "borderColor": "#A2CDED",
                "cornerRadius": "10px"
            }
        }
        return dataProfile
    
    def second_toggle(self, text, toggle=True):
        if toggle: picture = "https://i.ibb.co/PD9LY4P/SoziOn.png"
        else: picture = "https://i.ibb.co/X2z7YQs/ACODE44-OFF.png"
        dataProfile = {
            "type": "box",
            "layout": "horizontal",
            "contents": [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "image",
                            "url": picture,
                            "aspectRatio": "1377:865",
                            "align": "center",
                            "gravity": "center",
                            "size": "xxs"
                        }
                    ],
                    "width": "28%",
                    "borderWidth": "1px",
                    "borderColor": "#A2CDED",
                    "cornerRadius": "10px"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": text,
                            "align": "end",
                            "gravity": "center",
                            "color": "#FFFFFF",
                            "weight": "bold",
                            "size": "xxs"
                        },
                        {
                            "type": "separator",
                            "color": "#A2CDED"
                        }
                    ]
                }
            ],
            "alignItems": "center",
            "margin": "xs"
        }
        return dataProfile

    def toggle_on_off(self, text, toggle=True):
        if toggle: picture = "https://i.ibb.co/PD9LY4P/SoziOn.png"
        else: picture = "https://i.ibb.co/X2z7YQs/ACODE44-OFF.png"
        dataProfile = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://i.ibb.co/fvWCTrF/ACODE44-CIRCUIT.jpg",
                        "size": "full",
                        "aspectRatio": "991:339",
                        "aspectMode": "cover",
                        "position": "absolute"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": picture,
                                        "aspectRatio": "1377:865",
                                        "align": "start",
                                        "offsetStart": "1%",
                                        "gravity": "center",
                                        "size": "xs"
                                    }
                                ],
                                "width": "28%"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": text,
                                        "align": "center",
                                        "gravity": "center",
                                        "color": "#FFFFFF",
                                        "weight": "bold",
                                        "size": "md"
                                    }
                                ]
                            }
                        ],
                        "backgroundColor": "#00000080",
                        "alignItems": "center"
                    }
                ],
                "paddingAll": "0%"
            }
        }
        return dataProfile

    def toggle_on_off2(self, text, text2, toggle=True):
        if toggle: picture = "https://i.ibb.co/PD9LY4P/SoziOn.png"
        else: picture = "https://i.ibb.co/X2z7YQs/ACODE44-OFF.png"
        dataProfile = {
            "type": "bubble",
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "image",
                        "url": "https://i.ibb.co/fvWCTrF/ACODE44-CIRCUIT.jpg",
                        "size": "full",
                        "aspectRatio": "991:339",
                        "aspectMode": "cover",
                        "position": "absolute"
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "image",
                                        "url": picture,
                                        "aspectRatio": "1377:865",
                                        "align": "start",
                                        "offsetStart": "1%",
                                        "gravity": "center",
                                        "size": "xs"
                                    }
                                ],
                                "width": "28%"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": text,
                                        "align": "center",
                                        "gravity": "center",
                                        "color": "#FFFFFF",
                                        "weight": "bold",
                                        "size": "md"
                                    },
                                    {
                                        "type": "text",
                                        "text": text2,
                                        "color": "#FFFFFF",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "xxs",
                                        "wrap": True
                                    }
                                ]
                            }
                        ],
                        "backgroundColor": "#00000080",
                        "alignItems": "center"
                    }
                ],
                "paddingAll": "0%"
            }
        }
        return dataProfile

    def countryCode(self):
        res = '\n   - af : afrikaans'
        res += '\n   - sq : albanian'
        res += '\n   - am : amharic'
        res += '\n   - ar : arabic'
        res += '\n   - hy : armenian'
        res += '\n   - az : azerbaijani'
        res += '\n   - eu : basque'
        res += '\n   - be : belarusian'
        res += '\n   - bn : bengali'
        res += '\n   - bs : bosnian'
        res += '\n   - bg : bulgarian'
        res += '\n   - ca : catalan'
        res += '\n   - ceb : cebuano'
        res += '\n   - ny : chichewa'
        res += '\n   - zh-cn : chinese (simplified)'
        res += '\n   - zh-tw : chinese (traditional)'
        res += '\n   - co : corsican'
        res += '\n   - hr : croatian'
        res += '\n   - cs : czech'
        res += '\n   - da : danish'
        res += '\n   - nl : dutch'
        res += '\n   - en : english'
        res += '\n   - eo : esperanto'
        res += '\n   - et : estonian'
        res += '\n   - tl : filipino'
        res += '\n   - fi : finnish'
        res += '\n   - fr : french'
        res += '\n   - fy : frisian'
        res += '\n   - gl : galician'
        res += '\n   - ka : georgian'
        res += '\n   - de : german'
        res += '\n   - el : greek'
        res += '\n   - gu : gujarati'
        res += '\n   - ht : haitian creole'
        res += '\n   - ha : hausa'
        res += '\n   - haw : hawaiian'
        res += '\n   - iw : hebrew'
        res += '\n   - hi : hindi'
        res += '\n   - hmn : hmong'
        res += '\n   - hu : hungarian'
        res += '\n   - is : icelandic'
        res += '\n   - ig : igbo'
        res += '\n   - id : indonesian'
        res += '\n   - ga : irish'
        res += '\n   - it : italian'
        res += '\n   - ja : japanese'
        res += '\n   - jw : javanese'
        res += '\n   - kn : kannada'
        res += '\n   - kk : kazakh'
        res += '\n   - km : khmer'
        res += '\n   - ko : korean'
        res += '\n   - ku : kurdish (kurmanji)'
        res += '\n   - ky : kyrgyz'
        res += '\n   - lo : lao'
        res += '\n   - la : latin'
        res += '\n   - lv : latvian'
        res += '\n   - lt : lithuanian'
        res += '\n   - lb : luxembourgish'
        res += '\n   - mk : macedonian'
        res += '\n   - mg : malagasy'
        res += '\n   - ms : malay'
        res += '\n   - ml : malayalam'
        res += '\n   - mt : maltese'
        res += '\n   - mi : maori'
        res += '\n   - mr : marathi'
        res += '\n   - mn : mongolian'
        res += '\n   - my : myanmar (burmese)'
        res += '\n   - ne : nepali'
        res += '\n   - no : norwegian'
        res += '\n   - ps : pashto'
        res += '\n   - fa : persian'
        res += '\n   - pl : polish'
        res += '\n   - pt : portuguese'
        res += '\n   - pa : punjabi'
        res += '\n   - ro : romanian'
        res += '\n   - ru : russian'
        res += '\n   - sm : samoan'
        res += '\n   - gd : scots gaelic'
        res += '\n   - sr : serbian'
        res += '\n   - st : sesotho'
        res += '\n   - sn : shona'
        res += '\n   - sd : sindhi'
        res += '\n   - si : sinhala'
        res += '\n   - sk : slovak'
        res += '\n   - sl : slovenian'
        res += '\n   - so : somali'
        res += '\n   - es : spanish'
        res += '\n   - su : sundanese'
        res += '\n   - sw : swahili'
        res += '\n   - sv : swedish'
        res += '\n   - tg : tajik'
        res += '\n   - ta : tamil'
        res += '\n   - te : telugu'
        res += '\n   - th : thai'
        res += '\n   - tr : turkish'
        res += '\n   - uk : ukrainian'
        res += '\n   - ur : urdu'
        res += '\n   - uz : uzbek'
        res += '\n   - vi : vietnamese'
        res += '\n   - cy : welsh'
        res += '\n   - xh : xhosa'
        res += '\n   - yi : yiddish'
        res += '\n   - yo : yoruba'
        res += '\n   - zu : zulu'
        res += '\n   - fil : Filipino'
        res += '\n   - he : Hebrew'
        return res