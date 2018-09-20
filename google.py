# Author - Shidong Sun
def google_vision():
    import io
    import os
    import PIL
    from PIL import ImageFont
    from PIL import Image
    from PIL import ImageDraw

    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types
   
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    i=0
    # Scan all files in the folder where the images from Twitter are stored
    folder=os.getcwd()+'/picture/'
    for root,dirname,filenames in os.walk(folder):  
        for filename in filenames:  
            if os.path.splitext(filename)[1]=='.jpg':
                i += 1
    print(i)

    # Keep sending images to google vision until there is no file left
    for k in range(1,i+1):
        file_name = os.path.join(os.path.dirname(__file__),folder+'%04d'%(k)+'.jpg')
        # Load the image into memory
        # The following 6 line credit to Google quick start
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()
        image = types.Image(content=content)
        # Run label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations
        print('Labels:')

        tag=[]
        # Save the all labels with the sequence of their possibilities
        for label in labels:
            tag.append(label.description)
        print(tag)
        l=len(tag)
        # Modify the imags and add labels on them
        folder2=os.getcwd()+'/picture2/'
        if not os.path.exists(folder2):
            os.makedirs(folder2)
        img=Image.open(folder+'%04d'%(k)+'.jpg')
        img=img.resize((720,720),resample=Image.LANCZOS)
        font = ImageFont.truetype("/usr/share/fonts/truetype/ttf-dejavu/DejaVuSans.ttf",40)
        draw = ImageDraw.Draw(img)
        for m in range(0,l):
            draw.text((0, 40*m),tag[m],(255,0,0),font=font)
        draw = ImageDraw.Draw(img)
        img.save(folder2+'%04d'%(k)+'.jpg')

if __name__ == '__main__':
    google_vision()
