import time
import random
import os
import Aicode
import re

# import numpy as np
# import cv2
# import imutils
# import pytesseract

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    "./ai-based-project-firebase-adminsdk-asvwh-f7f9789ce2.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

try:
    # ADD CLIENT
    # doc_ref = db.collection(u'users').document(u'alovelace')

    # doc_ref = db.collection(u'users').document()
    # doc_ref.set({
    #     u'name': u'Lily',
    #     u'age': 29,
    #     u'gender': u'male',
    #     u'born': 1961,
    #     u'address': u'Pune',
    #     u'previousHistory': u'Yes',
    #     u'disease': u'LungDisease',
    #     u'amount': 200000,
    # })

    # FETCH ALL CLIENT
    # users_ref = db.collection(u'users')
    # docs = users_ref.stream()

    # for doc in docs:
    #     print(u'{} => {}'.format(doc.id, doc.to_dict()))

    print("WELCOME TO THE INSURANCE POLICY SOFTWARE\n")
    time.sleep(2)
    print("Type 1. 2. 3. to choose one of the following options:")
    print(
        "1. Add new document to be processed\n2. Check the status of a submitted document\n3. Close the software"
    )
    num = input("Enter your choice: ")
    if num == "1":
        while True:
            print("Drag the document into the UPLOAD folder.\n")
            time.sleep(10)
            if len(os.listdir('../../../../UPLOAD')) == 0:
                print("Directory is empty!\n")
                time.sleep(1)
                print("1.Upload another document\n2.Exit the software")
                option = input("Enter your choice: ")
                if option == "1":
                    continue
                else:
                    exit()
            else:
                print("Document is being checked by the software.")

                # scanning document

                # # read the image
                # image = cv2.imread(../../../../UPLOAD)
                # orig = image.copy()

                # # convert image to gray scale. This will remove any color noise
                # grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                # # Using cv2.imwrite() method
                # # Saving the image
                # cv2.imwrite(r'C:\Users\mukes\Desktop\discharge_gray.jpg', grayImage)

                # cv2.waitKey(0)  # press 0 to close all cv2 windows
                # cv2.destroyAllWindows()

                # # Converting image to text
                # pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
                # path = r'C:\Users\mukes\Desktop\discharge_gray.jpg'
                # img = cv2.imread(path)
                # text = pytesseract.image_to_string(img)
                # print(text)

                break
        print("Sending document.....")
        try:
            mylines = []  # Declare an empty list named mylines.
            with open('../../../../UPLOAD/doc.txt',
                      'rt') as myfile:  # Open lorem.txt for reading text data.
                for myline in myfile:  # For each line, stored as myline,
                    mylines.append(myline)  # add its contents to mylines.
                A = mylines[16][15:].strip()
                mylines[18][6:].strip()
                mylines[20][10:].strip()
                mylines[22][15:].strip()
            docs = db.collection(u'users').limit(1).where(u'name', u'==',
                                                          A).stream()
            for doc in docs:
                if (doc.to_dict()['age'] == int(mylines[18][6:].strip())):
                    if (doc.to_dict()['address'] == mylines[20][10:].strip()):
                        print("{}'s information has been updated".format(A))
        except:
            print("error")
        time.sleep(2)
        print("Processing.....")
        time.sleep(5)
        print("Fetching result.....")
        time.sleep(1)

        # Open the file that you want to search
        f = open("./UPLOAD/doc.txt", "r")

        # Will contain the entire content of the file as a string
        content = f.read()

        # The regex pattern that we created
        pattern = "\d{2}[/-]\d{2}[/-]\d{4}"

        # Will return all the strings that are matched
        dates = re.findall(pattern, content)
        a = dates[0]
        A = int(a[1:2])
        b = dates[1]
        B = int(b[1:2])
        if B - A >= 1:
            print(
                "The claim has been accepted and the amount will be processed to the connected bank account."
            )
        else:
            print(
                "The claim has been rejected by the software.\nFor further inquery please contact our customer representative at your nearest branch."
            )
        os.remove("./UPLOAD/doc.txt")

    elif num == "2":
        print("Please wait till we check the status.")
    else:
        exit()
except:
    print("Error occured")
