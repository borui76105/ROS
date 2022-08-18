#!/usr/bin/env python3
import threading
import rospy
from assignment1.msg import Chat

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    rospy.loginfo("{}: I heard {} from {}".format(rospy.get_caller_id(),
                                                  data.message,
                                                  data.author))

def listener():
    # nodes will be assigned a unique name if anonymous=True 
    # so that multiple listeners can run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("chatter", Chat, callback)
    rospy.spin() # keeps node alive until shutdown signal received

def talker():
    pub = rospy.Publisher('chatter', Chat, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    chat = Chat(author=rospy.get_name()) # create message object

    while not rospy.is_shutdown():
        chat.header.stamp = rospy.Time.now() # update timestamp of message
        chat.message = input() # wait for user input, update message field
        pub.publish(chat)      # publish message    

def user():
    pub = rospy.Publisher('chatter', Chat, queue_size=10)
    rospy.init_node('user', anonymous=True)
    rospy.Subscriber("chatter", Chat, callback)
    chat = Chat(author=rospy.get_name()) # create message object

    while not rospy.is_shutdown():
        chat.header.stamp = rospy.Time.now() # update timestamp of message
        chat.message = input() # wait for user input, update message field
        pub.publish(chat)      # publish message    

user()