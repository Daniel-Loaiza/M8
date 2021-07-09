import json, requests, urllib
import os
import pandas as pd

def findPlayers():
    """Searches through NBA player heights based on user input.
    
    The function receives a single integer input. Then it prints
    a list of all pairs of players whose height in inches adds up 
    to the integer input to the application. If no matches are 
    found, the application will print "No matches found".
    
    Typical usage example:
    
    Type a number
    >139
    
    -Nate Robinson	Mike Wilks
    -Nate Robinson	Brevin Knight
    
    Args:
        height: A decimal positive integer.
        
    """
    
    url = 'https://mach-eight.uc.r.appspot.com/'
    response = urllib.request.urlopen(url)
    data = json.loads(response.read()) # Download data from website
    df = pd.DataFrame(data['values']) # Transform data into pandas DataFrame

    convert_dict = {'first_name':str,
                'h_in':int,
                'h_meters':float,
                'last_name':str}

    df = df.astype(convert_dict)

    df=df.sort_values(by=['h_in']) #Sort pandas DataFrame with time complexity O(NlogN)
    df.reset_index(drop=True, inplace=True)
    
    try:
        
        height = int(input("Type a number\n"))

        # Check input
        if isinstance(height, int)!=True:
            raise TypeError('Work with Numbers Only')
        elif height < 0:
            raise ValueError('Work with Positive Numbers Only')
        else:
            counter = 0
            left = 0
            right = df.shape[0]-1
            temp=right
            while(left<right): #Notice we are only using a While loop (Two embedded for loops would take a time complexity of O(N**2)
                if((df['h_in'][left]+df['h_in'][right])>height):
                    right -= 1
                    temp=right
                elif ((df['h_in'][left]+df['h_in'][right])<height):
                    left += 1
                elif((df['h_in'][left]+df['h_in'][right])==height):
                    counter +=1
                    print("-{} {}\t{} {}".format(df['first_name'][left],df['last_name'][left],df['first_name'][right],df['last_name'][right]))
                    right -= 1
                    if(left==right):
                        right=temp
                        left += 1
            if counter==0:
                print("No matches found")
    except ValueError as ve:
        print('You are supposed to enter positive number.')
    input()
            
if __name__=="__main__":
    findPlayers()
