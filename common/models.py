from django.db import models

# Create your models here.

class SponsorAd(models.Model):
    COLOR_CHOICES = (
        ('RED', 'red'),
        ('WHITE', 'white'),
        ('BLUE', 'blue'),
    )

    POSITION_CHOICES=( ("TOP","top"),("MIDDLE","middle"),("BUTTOM","buttom"))
    
    file = models.FileField(upload_to ='uploads/')
    ref_slug= models.CharField(max_length=100, blank=True, null=True) 
    ads_url= models.URLField(blank=True, null=True)  
    border_height=models.IntegerField(default=200)
    border_width=models.IntegerField(default=1000)
    img_height=models.IntegerField(default=180)
    img_width=models.IntegerField(default=990)
    border_color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='RED')
    position = models.CharField(max_length=50, choices=POSITION_CHOICES, default='TOP')
    
    body=models.TextField(max_length=9999999, blank=True, null=True)
    visibility=models.BooleanField(default=False)
    Test_demo_url= models.URLField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(blank=True, auto_now=True, null=True)
    def __str__(self):
        return f"{self.ref_slug}"
    
    
    
    
    def save(self, *args, **kwargs):
        
        code="""<br /><br />
            <a class="fragment" 
            style="font-size: 12px;
            font-family: tahoma;
            height: """+ str(self.border_height) +"""px;
            width: """+str(self.border_width) +"""px;
            border: 1px solid #ccc;
            color: #555;
            display: block;
            padding: 5px;
            box-sizing: border-box;
            text-decoration: none;"
            target="_blank" href='"""+str(self.ads_url)+"""' onclick="dataLayer.push({'event': 'adult_time'})" >
                <div>
                    <span
                    style="float:right;
                    display:inline-block;
                    padding:2px 5px;
                    background:#ccc;"
                    id='close' onclick='this.parentNode.parentNode.parentNode.removeChild(this.parentNode.parentNode); return false;'>x</span>
                <img
                style="float: left;
                margin-right: 1px;
                height: """+ str(self.img_height) +"""px;
                width: """+ str(self.img_width) +"""px;"
                src ='"""+str(self.file.url)+"""' alt="some description"/> 

            </div>
            </a>"""
        self.body=code
        self.Test_demo_url=f"https://www.sbsy.co.in/show_ads/{self.id}"

        return super(SponsorAd, self).save(*args, **kwargs)



        
