# myblog
bootstrap front end

图片上传
1. models.py
    img = models.ImageField(upload_to='img/%Y/%m/%d')
2. settings.py
    TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [ os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                ...
                'django.template.context_processors.media',
            ],
        },
    },
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace("\\", '/')

3. 前端
    ···<img src="{{ MEDIA_URL }}{{ article.img }}" class="img-responsive" alt="img"></a>···
  
  


