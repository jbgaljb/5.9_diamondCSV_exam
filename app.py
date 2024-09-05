# hands off Chat GPT, beside the README

import pandas as pd

df = pd.read_csv('data.csv')

def mostExpensive():
    return str(df.price.max())

def averagePrice(): # division of sum price / number of diamonds
    return str(df.price.sum() /  len(df.transpose().columns))

def idealCount(): # count of filtered "IDEAL" cut
    return str(len(df.loc[df['cut'] == 'Ideal']))

def differentColors(): # returns a list of the different colors
    return df.color.unique().tolist()

def premiumCaratMedian(): # carat median of Premium cut
    return str(df.loc[df['cut'] == 'Premium'].carat.median())

def averageCaratHelper(cut):
    cutTable = df.loc[df['cut'] == cut] # creates df with the param cut diamonds
    return cutTable.carat.sum() / len(cutTable)

def averageCaratPerCut():
    for cut in df.cut.unique(): # loop over the cut types
        print("Cut: " + cut + " || Average: " +  str(averageCaratHelper(cut)))

def averagePriceHelper(color):
    colorTable = df.loc[df['color'] == color] # creates df with the param color diamonds
    return colorTable.price.sum() / len(colorTable)

def averagePricePerColor():
    for color in df.color.unique():
        print("color: " + color + " || price: " +  str(averagePriceHelper(color)))



def main():
    print("The price of the most expensive diamond is: " +
           mostExpensive() + "\n")
    
    print("The average price is: " + averagePrice() + "\n")

    print("The number of Ideal cut diamonds is: " + idealCount() + "\n")

    print("The " + str(len(differentColors())) + " distinct colors are: " + 
          ', '.join(differentColors()) + "\n") 

    print("The median carat of the Premium cut diamonds is: " + 
    premiumCaratMedian() + "\n")

    print("The carat average per cut are: ")
    averageCaratPerCut()
    print("")

    print("The average price per color is: ")
    averagePricePerColor()


if __name__ == "__main__":
    main()
