**Глава 1: Введение**

*1.1 Цель и актуальность работы*

С постоянным развитием медицинской технологии и внедрением новых методов диагностики, специалисты все чаще сталкиваются
с потребностью в обмене информацией, опытом и конкретными примерами описания и интерпретации различных методов
исследования. К примеру среди этих исследований можно выделить основную группу - методы лучевой диагностики, среди
которых выделяют основные: классический рентген, компьютерную томографию (КТ), магнитно-резонансную томографию (МРТ).
Также к этой группе можно отнести ПЭТ КТ, рентгеноскопические исследования и рентгенологические исследования с 
введением контрастного вещества (ирригоскопия, скопия пищевода и желудка, гистеросальпингография, фистулография и тд), 
маммографию, флюорографию, рентгенографические исследования в стоматологии: КЛКТ, ортопантомографию, 
прицельные рентгеновские снимки.

В данный момент времени, проработав 3 года врачом-рентгенологом могу сказать, что на своих рабочих местах у меня и моих
коллег не было удобной системы, для хранения шаблонов описаний рентгенологических исследований (многие АРМ врачей не
предоставляют доступ пользователю к операционной системе и не имеют возможности "из коробки" для сохранения стандартных
шаблонов описаний - на них приходится постоянно печатать текст описания заново, что при объеме одного описания в
зависимости от типа исследования может составлять от 0,5 до 1 страницы текста А4, а при потоке пациентов от 60 до 100
человек за смену в 6 часов только усложняет работу и замедляет выдачу большинства типовых описаний. Там, где рабочее место
представлено обычным компьютером - чаще удобнее оказывалось хранить описания в отдельных .docx файлах, тем не менее,
это не очень удобно для поиска, особенно на устаревших машинах).

Таким образом моя работа представляет собой создание платформы, обеспечивающей различным медицинским специалистам
(врачам-рентгенологам, студентам и ординаторам медицинских ВУЗов, преподавателям) удобное хранилище шаблонов описаний
лучевых (а в частности различных рентгеновских) методов исследования, с возможностью просмотра сохраненных описаний,
добавления новых, поиску в базе по названию описания, фильтрации по различным полям для удобного поиска и тд.

*1.2 Описание проблемы*

На сегодняшний день существует множество медицинских учреждений и образовательных организаций, где проходят исследования,
а также множество медицинских ВУЗов, где преподаются курсы по рентгенологии. Однако, как я и описал выше - централизованной
базы данных, где были бы собраны типовые и нестандартные примеры описаний рентгеновских исследований, в них нет.
Тем не менее, ее создание сделает работу медицинских специалистов гораздо проще, как минимум освободив им много времени,
которое они могли бы потратить на поиск среди тысяч файлов нужного описания, либо печатая его каждый раз заново вручную.
А чем больше времени остается у врача свободным от ведения огромного количества документации в медицине - тем больше
времени он может посвятить детальному изучению исследования каждого пациента, более персональному подходу к нему и
оказанию качественной и персонализированной медицинской помощи.

*1.3 Основные задачи*

Среди задач, которые я поставил перед собой в ходе написания данной работы и самой платформы были:
- Разработка архитектуры веб-платформы, обеспечивающей хранение, добавление и просмотр различных описаний рентгеновских
исследований.
- Создание простого, минималистичного и дружественного UI для удобного доступа к данным, поиска и фильтрации данных.
- Разработка системы авторизации и аутентификации пользователей, настройка прав доступа для различных ролей пользователей:
  основной функционал платформы доступен только авторизованным пользователям, а полный функционал с редактированием
  объектов в базе данных только для суперпользователей(админов).

*1.4 Предполагаемые результаты*

В результате выполнения дипломной работы будет разработан сайт, который станет надежным и удобным инструментом для
медицинских специалистов разных уровней. Этот сайт позволит пользователям не только просматривать имеющиеся шаблоны
описаний и осуществлять быстрый поиск и удобно фильтровать список всех описаний, но и добавлять свои собственные,
тем самым обогащая базу данных и расширяя возможности коллег, делясь с ними своими знаниями.

*1.5 Структура работы*

Данная дипломная работа состоит из трех глав:

- Введение, где обосновывается актуальность выбранной темы и ставятся основные задачи.
- Разработка и реализация проекта, включая этапы проектирования, разработки и тестирования веб-платформы.
- Оценка и обоснование ценности проекта, где проводится анализ потенциальной полезности сайта для медицинского 
сообщества и образовательных учреждений.

---

**Глава 2: Разработка и реализация проекта**

*2.1 Архитектура веб-платформы*

*2.1.1 Выбор технологий*

Платформа написана с использованием языка программирования Python, и фреймворков Django и DjangoRestFramework. 
Python - это мощный и гибкий язык программирования, который позволяет быстро создавать практически что угодно, 
в том числе он подойдет и для разработки сложных веб-приложений. Он относится к интерпретируемым, поэтому его код при
запуске читается и выполняется построчно, в отличие от компилируемых языков, к примеру Java.
В моем случае я использовал стандартную версию интерпретатора Python, которая предоставляется "из коробки" вместе с
дистрибутивом Ubuntu 22.04 - Python 3.10. В Ubuntu она необходима для функционирования самой операционной системы, 
именно поэтому интерпретатор Python уже в нее встроен.

Django и DjangoRestFramework - это высокоуровневые веб-фреймворки, который значительно упрощает процесс разработки сайтов.
Чтобы создать проект, для начала мне нужно было создать для него свою виртуальную среду, Pycharm, который я использовал
для разработки, создает ее автоматически, тем не менее, вручную создать ее довольно легко, использовав в терминале команду
python3 -m venv и добавить название своей виртуальной среды, допустим, тот же venv. Таким образом вся команда в этом 
случае будет выглядеть python3 -m venv venv. Не всегда происходит автоматический переход в той же вкладке терминала сразу
в виртуальную среду, поэтому иногда его нужно будет перезапустить.

Далее нам нужно установить в виртуальную среду наши фреймворки, для чего я воспользовался pip. Команды для их установки 
будут выглядеть следующим образом: pip install django, pip install djangorestframework. При необходимости после указания
названия того пакета, который мы устанавливаем, можно через == указать необходимую нам версию (в данном случае фреймворки
были установлены без их указания, т.е. с использованием последних версий).

Также стоит упомянуть базу данных, для наших учебных целей вполне хватит использования SQLite3. В дальнейшем, если 
развивать проект, можно подумать об использовании и других БД, к примеру тот же PostgreSQL, который достаточно часто 
входит в технологический стек многих проектов. Тем не менее, SQLite3 идет "из коробки" с Django и не требует 
дополнительной установки.

Остальной стек необходимых зависимостей был указан в requirements.txt, были использованы:
- django-filter - для более удобного создания собственных фильтров, которые были реализованы на списочной 
странице описаний
- drf-yasg - для создания автодокументации API проекта
Они были установлены аналогично фреймворкам с помощью команд pip install django-filter и pip install drf-yasg соответственно.

Далее для удобства развертывания проекта в дальнейшем на других системах был создан файл requirements.txt, в котором
отражены необходимые зависимости для работы проекта, а создан он был с помощью команды pip freeze > requirements.txt,
выполненной из директории проекта. Но чаще таким образом туда могут попадать малозначимые для работы приложения зависимости,
либо же вообще не используемые, но находящиеся в нашей виртуальной среде, чтобы этого избежать в pycharm есть удобная
функция Sync Python Requirements, находящаяся в выпадающем вкладке Tools слева вверху, в которой можно включить чекбокс,
который удалит из этого списка зависимостей неиспользуемые.

*2.1.2 Создание проекта и приложений в Django*

Далее нам необходимо создать свой проект в Django. Для этого мы воспользуемся командой django-admin startproject и далее
вводится имя проекта. В моему случае полная команда с учетом названия проекта radiology_sample будет выглядеть следующим 
образом: django-admin startproject radiology_sample.

После выполнения этой команды у нас появятся следующий каталоги: radiology_sample, который будет содержать в себе файл 
manage.py и каталог radiology_sample как наше основное приложение django, с settings.py и urls.py (из наиболее значимых
для нас на данный момент).

После этого мы можем с помощью команды cd radiology_sample "упасть" внутрь нашего проекта и создать в нем наше первое
приложение, которое будет отражать нашу основную сущность в базе данных и логике проекта - sample, или шаблон описания.
Создаем его с помощью команды django-admin startapp sample, получаем каталог внутри нашего проекта с названием sample,
который содержит в себе основные файлы для работы этого приложения: admin.py, apps.py, models.py, tests.py, views.py.

Созданное нами приложение sample мы должны добавить в settings.py в INSTALLED_APPS, также нам надо его зарегистрировать
в apps.py в нашем каталоге sample.

Делаем мы это следующим образом:

- В settings.py в INSTALLED_APPS пишем:

        INSTALLED_APPS = [
        ...
        'sample',
        ...
        ]

- В apps.py:
  
      from django.apps import AppConfig
        
        
      class SampleConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'sample'

Далее мы можем перейти к созданию нашей основной модели этого приложения, которую мы назовем также Sample. Создаем ее в
models.py в директории sample, используя следующий код:

from django.db import models


    class Sample(models.Model):
        MODALITY_CHOICES = (
            ("RG", "Рентген"),
            ("CT", "КТ"),
            ("MRI", "МРТ"),
        )
    
        REGION_OF_INTEREST_CHOICES = (
            ("HEAD", "Голова"),
            ("NECK", "Шея"),
            ("THORAX", "Грудная клетка"),
            ("ABDOMEN", "Брюшная полость"),
            ("LIMBS", "Конечности"),
        )
    
        SPECIALIZATION_CHOICES = (
            ("TRAUMA", "Травматология"),
            ("PHYSICIAN", "Терапия/педиатрия"),
            ("OTOLARYNGOLOGY", "Оториноларингология"),
            ("NEUROLOGY", "Неврология"),
            ("ONCOLOGY", "Онкология"),
        )
    
        title = models.CharField(max_length=256, verbose_name='Заголовок описания',
                                 blank=False, null=False)
        text = models.TextField(verbose_name='Текст описания', blank=False, null=False)
        datetime_of_creation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
        datetime_of_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
        modality = models.CharField(verbose_name='Модальность исследования', max_length=50, choices=MODALITY_CHOICES,
                                    default="", blank=False, null=False)
        region_of_interest = models.CharField(verbose_name='Зона исследования', max_length=50,
                                              choices=REGION_OF_INTEREST_CHOICES, default="", blank=False, null=False)
        specialization = models.CharField(verbose_name='Специализация', max_length=50, choices=SPECIALIZATION_CHOICES,
                                          default="", blank=False, null=False)

Теперь более подробно разберем представленный код:

Мы создаем класс Sample, наследуя его от models.Model из django.db.

После чего мы сможем задавать нашей модели в базе данных нужные нам поля. В начале мы формируем три класса _CHOICES, 
которые представляют из себя кортеж кортежей из двух элементов, первый из них будет записываться непосредственно как 
выбранное значение поля в базу данных, а второй представляет из себя его человекопонятное представление.

Данные кортежи кортежей лягут в основу полей modality, region_of_interest, specialization и будут использоваться как
значения для селектов в выпадающем списке. Также мы указываем этим полям параметры blank=False, null=False, т.к.
считаем, что для каждого шаблона описания исследования должны быть обязательно указаны данные параметры, что облегчит
в дальнейшем нам и пользователям фильтрацию для поиска нужного шаблона описания на списочной странице шаблонов описаний.
Благодаря параметрам verbose_name= и max_length= мы задаем название, которое будет отображаться у поля в админке и
в формах в будущем, чтобы оно имело человекопонятный вид, а также максимальную длину, которое хранит это поле CharField,
соответственно. 

Поле title также относится к типу CharField, содержит в себе буквенное отображение заголовка шаблона описания в базе 
данных, ограниченное длиной содержимого в 256 символов и также является обязательным для заполнения и не может содержать
в себе Null значения.

Поле text представляет из себя сам текст шаблона описания исследования, представлено типом TextField - большим по
объему данных текстовым полем, максимальный размер которого зависит от базы данных, используемой для реализации проекта.
Оно также не может быть пустым и хранить в себе Null.

И далее два поля, представленные типом DateTimeField, datetime_of_creation и datetime_of_change. В случае поля даты
создания используется автоматическое проставление времени создания благодаря параметру auto_now_add=True, т.е. при
создании экземпляра модели Sample в базе данных будет автоматически установлено время его создания. В случае поля даты
изменения используется параметр auto_now=True, который также проставит время автоматически, но только в момент очередного
сохранения экземпляра модели, т.е. при внесении в существующую запись каких-либо изменений.

Создав данную модель, нам следует зарегистрировать ее в admin.py нашего приложения. Для этого используем следующий код:

        from django.contrib import admin
        from .models import Sample
        
        
        @admin.register(Sample)
        class SampleAdmin(admin.ModelAdmin):
            pass

Теперь нам надо приступить к реализации основных функций нашего приложения для взаимодействия с этой моделью, т.е.
созданию API. Мы будем создавать их в в файле views.py. Для этого используем следующий код:

    from rest_framework.decorators import action
    from rest_framework.renderers import TemplateHTMLRenderer
    from rest_framework.response import Response
    from rest_framework.viewsets import GenericViewSet
    from .serializers import SampleSerializer
    from .models import Sample
    from django.shortcuts import render
    from .forms import SampleForm
    from django_filters import rest_framework as filters
    from rest_framework import mixins
    from rest_framework.permissions import IsAuthenticated
    
    
    class SampleFilter(filters.FilterSet):
        title = filters.CharFilter(lookup_expr='icontains')
        modality = filters.ChoiceFilter(choices=Sample.MODALITY_CHOICES)
        region_of_interest = filters.ChoiceFilter(choices=Sample.REGION_OF_INTEREST_CHOICES)
        specialization = filters.ChoiceFilter(choices=Sample.SPECIALIZATION_CHOICES)
    
        class Meta:
            model = Sample
            fields = ['title', 'modality', 'region_of_interest', 'specialization']
    
    
    class SampleViewSet(mixins.ListModelMixin, GenericViewSet):
        permission_classes = [IsAuthenticated]
        queryset = Sample.objects.all()
        serializer_class = SampleSerializer
        filter_backends = (filters.DjangoFilterBackend,)
        filterset_class = SampleFilter
        search_fields = ('title',)
    
        @action(methods=['get'], detail=False)
        def get_all_samples(self, request):
            queryset = Sample.objects.all()
            title_search = request.GET.get('title_search', None)
            if title_search:
                title_search = title_search.lower()
            modality_filter = request.GET.get('modality_filter', None)
            region_of_interest_filter = request.GET.get('region_of_interest_filter', None)
            specialization_filter = request.GET.get('specialization_filter', None)
            if title_search:
                queryset = queryset.filter(title__icontains=title_search)
            if modality_filter:
                queryset = queryset.filter(modality=modality_filter)
            if region_of_interest_filter:
                queryset = queryset.filter(region_of_interest=region_of_interest_filter)
            if specialization_filter:
                queryset = queryset.filter(specialization=specialization_filter)
            ordering = request.GET.get('ordering', '')
            if ordering:
                queryset = queryset.order_by(ordering)
            samples = queryset.values()
            context = {
                'samples': samples,
                'MODALITY_CHOICES': Sample.MODALITY_CHOICES,
                'REGION_OF_INTEREST_CHOICES': Sample.REGION_OF_INTEREST_CHOICES,
                'SPECIALIZATION_CHOICES': Sample.SPECIALIZATION_CHOICES,
                'ordering': ordering,
            }
            return render(request, 'sample/get_all_samples.html', context)
    
        @action(methods=['get'], detail=True)
        def get_defined_sample(self, request, pk):
            defined_sample = Sample.objects.get(pk=pk)
            return render(request, 'sample/get_defined_sample.html',
                          {'defined_sample': SampleSerializer(defined_sample).data})
    
        @action(detail=False, methods=['get', 'post'], renderer_classes=[TemplateHTMLRenderer])
        def add_sample(self, request):
            if request.method == 'POST':
                form = SampleForm(request.POST)
                if form.is_valid():
                    form.save()
                    return Response({"message": "Описание успешно добавлено!"},
                                    template_name='rest_framework/success_template.html')
            else:
                form = SampleForm()
            return Response({'form': form}, template_name='rest_framework/sample_form.html')

Теперь перейдем к разбору данного кода:

Начнем с класса SampleViewSet. Он наследуется в нашем случае от mixins.ListModelMixin и GenericViewSet.
GenericViewSet нужен нам как базовый класс для создания любого кастомного ViewSet, а ListModelMixin реализует 
собой представление нашего queryset в формате списка. В SampleViewSet мы указываем permission_classes = [IsAuthenticated],
чтобы доступ к основному функционалу нашего API (просмотру списочной страницы описаний, добавлению новых описаний и
просмотру конкретного описания мог получить доступ только аутентифицированный пользователь - остальные увидят ошибку 403
Forbidden). Параметр queryset отображает какие именно объекты модели мы получим для дальнейшего взаимодействия с ними в
рамках наших запросов к базе данных через django ORM. В нашем случае он представлен Sample.objects.all(), т.е. получает 
все экземпляры модели, хранящиеся в нашей базе данных. Далее мы указываем класс сериалайзера, в нашем случае это 
SampleSerializer, код которого находится в serializers.py нашего приложения, вот он:

    from rest_framework import serializers
    from .models import Sample
    
    
    class SampleSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Sample
            fields = ('title', 'text', 'datetime_of_creation', 'datetime_of_change',
                      'modality', 'region_of_interest', 'specialization')

С его помощью мы указываем модель Sample и определенный набор ее полей для сериализации и десериализации данных 
(т.е для перевода данных в битовое представление, либо наоборот, соответственно), представленных в нашей модели.
Далее мы прописываем параметры filter_backends = (filters.DjangoFilterBackend,), filterset_class = SampleFilter и 
search_fields = ('title',), которые будут указывать нам, какие фильтры мы хотим использовать. В данном случае несколько 
выше в коде у нас представлен SampleFilter, который определяет поля нашей модели, по которым будет осуществляться фильтрация
а также поиск (по полю title).

Теперь перейдем к основному функционалу нашей платформы, который будет лежать в основе эндпоинтов данного приложения.

Начнем с функции get_all_samples. Она формирует queryset всех объектов класса Sample и дальше начинаются проверки,
передано ли нам с фронта такие поля как title_search, modality_filter, region_of_interest_filter и specialization_filter.
Если они переданы, мы формируем новый queryset, производя фильтрацию по указанным полям и переданным с фронта данным.
Если они не переданы, то у нас остается полный набор экземпляров модели Sample. Далее мы передаем эти данные в контекст
шаблона и на их основе с помощью функции render отдаем эти данные на фронт в темплейт get_all_samples.html.

Далее у нас идет функция get_defined_sample, которая гораздо короче и ее основная суть - получить экземпляр модели Sample
по его pk(PrimaryKey), который будет получен с фронта и передать данные это экземпляра в темплейт get_defined_sample.html
с помощью функции render

И наконец остается функция add_sample, которая отвечает за добавления нового экземпляра модели Sample, используя кастомную 
форму SampleForm, данные которой передаются в темплейт sample_form.html с помощью функции render, а при успешном
заполнении формы с учетом стандартных валидаций Django пользователь будет направлен на темплейт success_template.html, а
данные из самой формы будут сохранены как новый экземпляр класса Sample.

Код данной формы находится в forms.py нашего приложения и представляет из себя:

    from django import forms
    from .models import Sample
    
    
    class SampleForm(forms.ModelForm):
        class Meta:
            model = Sample
            fields = '__all__'

В нем мы указываем, что форма наследуется от forms.ModelForm и содержит в себе все поля модели Sample.

Таким образом, прописав функционал нашего API для приложения Sample мы должны добавить их в urls.py нашего основного 
приложения radiology_sample.

    from django.contrib import admin
    from django.urls import path, include, re_path
    from django.views.generic import TemplateView
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi
    from rest_framework import routers
    from sample.views import SampleViewSet  # noqa
    from account.views import CreateUserView  # noqa
    from django.contrib.auth.views import LoginView
    
    router = routers.SimpleRouter()
    router.register(r'sample', SampleViewSet)
    
    schema_view = get_schema_view(
       openapi.Info(
          title="Snippets API",
          default_version='v1',
          description="Test description",
          terms_of_service="https://www.google.com/policies/terms/",
          contact=openapi.Contact(email="contact@snippets.local"),
          license=openapi.License(name="BSD License"),
       ),
       public=True,
       permission_classes=[permissions.AllowAny],
    )
    
    urlpatterns = [
        path('', TemplateView.as_view(template_name='index.html')),
        path('admin/', admin.site.urls),
        path('api/v1/auth/login/', LoginView.as_view(template_name='rest_framework/custom_login.html'), name='login'),
        path('api/v1/auth/', include('rest_framework.urls')),
        path('api/v1/', include(router.urls)),
        path('api/v1/registration', CreateUserView.as_view()),
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]

В нем мы создаем роутер и регистрируем его с помощью router = routers.SimpleRouter() и router.register(r'sample', SampleViewSet).
Так у нас из нашего SampleViewSet будут автоматически созданы эндпоинты с названиями, которые соответствуют функциям 
нашего ViewSet, а с помощью r'sample' мы задаем им имя, которое будет стоять в url эндпоинтов перед названиями этих функций.
Далее добавляем наш роутер в urlpatterns как path('api/v1/', include(router.urls)), что в итоге сформирует нам эндпоинты
localhost:8000/api/v1/sample/get_all_samples, localhost:8000/api/v1/sample/<pk>/get_defined_sample и
localhost:8000/api/v1/sample/add_sample.

Также здесь отражено подключение эндпоинтов drf-yasg(swagger) для автодокументации API, которые устанавливаются просто
согласно технической документации. Другая часть эндпоинтов создается django автоматически. Для эндпоинта 
path('api/v1/auth/login/', LoginView.as_view(template_name='rest_framework/custom_login.html'), name='login'),
был просто переделан темплейт, чтобы он внешне соответствовал стилистике сайта. А вот эндпоинт 
path('api/v1/registration', CreateUserView.as_view()), кастомный, поэтому перейдем к нему.

Для более удобной регистрации пользователей, реализации возможности login и logout было создано приложение account
аналогичным образом как и предыдущее, с помощью команды django-admin startapp account из корневой директории проекта.
Далее оно было зарегистрировано в apps.py

    from django.apps import AppConfig
    
    
    class AccountConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'account'

и добавлено в INSTALLED_APPS в settings.py

    INSTALLED_APPS = [
        ...
        'account',
    ]

для регистрации пользователей через кастомную форму нам потребуется создать ее в forms.py:

    from django import forms
    from django.contrib.auth.models import User
    
    
    class UserRegistrationForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput, label='Пароль:')
        username = forms.CharField(help_text="", label='Имя пользователя:')
    
        class Meta:
            model = User
            fields = ['username', 'password']

в ней мы указываем два поля для создания на основе введенных в них данных экземпляра модели User, также задавая им
кастомные лейблы, чтобы придерживаться общего стиля. На основе этой формы и будет построено наше представление 
CreateUserView:

    from django.views.generic.edit import CreateView
    from django.contrib.auth import get_user_model
    from .forms import UserRegistrationForm
    from django.urls import reverse_lazy
    
    
    class CreateUserView(CreateView):
        model = get_user_model()
        form_class = UserRegistrationForm
        template_name = 'account/registration.html'
        success_url = reverse_lazy('rest_framework:login')

Здесь мы указываем,  что в качестве модели пользователя мы берем стандартную модель из django, с помощью параметра 
form_class связываем это представление с описанной выше новой кастомной формой. Параметр template_name указывает, что
в качестве темплейта для этого представления будет выступать созданный нами registration.html, а в случае успешного
заполнения формы, создания экземпляра модели пользователя мы будем переброшены на страницу для login.

На данный момент backend часть нашего приложения готова, чтобы покрыть основной API - SampleViewSet unit-тестами, они были
написаны в каталоге приложения sample в файле tests.py:

    from django.test import TestCase
    from rest_framework import status
    from rest_framework.test import APIClient
    from .models import Sample
    from django.contrib.auth import get_user_model
    
    
    class SampleViewSetTestCase(TestCase):
        def setUp(self):
            self.client = APIClient()
            user_model = get_user_model()
            user = user_model.objects.create(username='testuser', password='testpassword')
            self.client.force_authenticate(user)
            self.sample_data = {
                'title': 'Test Title',
                'text': 'Test Text',
                'modality': 'RG',
                'region_of_interest': 'HEAD',
                'specialization': 'TRAUMA'
            }
            self.sample = Sample.objects.create(**self.sample_data)
    
        def test_get_all_samples(self):
            response = self.client.get('/api/v1/sample/get_all_samples/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.context['samples']), 1)
    
        def test_add_sample(self):
            new_sample_data = {
                'title': 'New Test Title',
                'text': 'New Test Text',
                'modality': 'CT',
                'region_of_interest': 'NECK',
                'specialization': 'PHYSICIAN'
            }
            response = self.client.post('/api/v1/sample/add_sample/', new_sample_data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(Sample.objects.count(), 2)
    
        def test_get_defined_sample(self):
            response = self.client.get('/api/v1/sample/1/get_defined_sample/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.context['defined_sample']['title'], self.sample_data['title'])
    
        def test_filters(self):
            Sample.objects.create(title='Another Title', text='Another Text', modality='MRI', region_of_interest='THORAX',
                                  specialization='NEUROLOGY')
    
            response = self.client.get('/api/v1/sample/get_all_samples/', {'title_search': 'Another Title'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.context['samples']), 1)
    
            response = self.client.get('/api/v1/sample/get_all_samples/', {'modality_filter': 'MRI'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.context['samples']), 1)
    
            response = self.client.get('/api/v1/sample/get_all_samples/', {'region_of_interest_filter': 'THORAX'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.context['samples']), 1)
    
            response = self.client.get('/api/v1/sample/get_all_samples/', {'specialization_filter': 'NEUROLOGY'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.context['samples']), 1)

        def test_get_all_samples_negative(self):
            self.client.logout()
            response = self.client.get('/api/v1/sample/get_all_samples/')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
        def test_add_sample_negative(self):
            self.client.logout()
            new_sample_data = {
                'title': 'New Test Title',
                'text': 'New Test Text',
                'modality': 'CT',
                'region_of_interest': 'NECK',
                'specialization': 'PHYSICIAN'
            }
            response = self.client.post('/api/v1/sample/add_sample/', new_sample_data)
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
        def test_get_defined_sample_negative(self):
            self.client.logout()
            response = self.client.get('/api/v1/sample/1/get_defined_sample/')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

Теперь можно перейти к их разбору:
Для начала нам нужно создать функцию def setUp, чтобы заложить изначальные настройки для тестирования. В ней мы создаем
своего тестового API клиента с помощью self.client = APIClient(). Далее получаем модель пользователя и создаем на ее
основе тестового пользователя, которого мы аутентифицируем вручную с помощью функции force_authenticate (без этого мы 
получим ошибки 403 Forbidden в тестах, согласно нашим правам доступа, указанным в SampleViewSet). А также создаем
тестовый экземпляр шаблона описания.
Первая группа тестов - позитивные, они проверяют, что каждый из эндпоинтов отвечает 200 HTTP Status Code, а также, что в
test_add_sample создается новый экземпляр модели Sample, а в случае с test_get_defined_sample получаем конкретный экземпляр,
тот, который мы и запрашивали. Тест test_filters, исходя из названия, проверяет фильтрацию и поиск, создавая новый объект
и убеждаясь, что фильтры возвращают корректное число ожидаемых экземпляров шаблона описаний.

Далее следует три негативных теста, основная задача которых проверить, что эндпоинты не "отдаются" неавторизованному
пользователю.
Вся суть тестов здесь - использование self.assertEqual(), которой мы передаем два параметра, и если они одинаковые,
как и ожидалось - мы получаем True и тест считается пройденным.


*2.1.2 Основной элемент базы данных*

Как уже описывалось выше, повторюсь, что основной элемент базы данных - это класс Sample, отражающий в себе поля
описания рентгеновского исследования, такие как:
- ID записи
- Заголовок описания
- Текст описания
- Модальность исследования (КТ, МРТ, классический рентген и др.)
- Зона интереса
- Специализация (в данном случае подразумевается для какой медицинской специальности характерна (или более характерна) 
патология, выявленная в исследовании и отраженная в тексте его описания)
- Дата добавления
- Дата изменения

*2.2 Интерфейс веб-платформы*

Здесь мы перейдем к реализации frontend части моей платформы. Верстка страниц была выполнена с помощью обычных
HTML и CSS, также был использован шаблонизатор Django. Также для правильного отображения человекопонятных значений 
кортежей в трех селектах модели Sample (modality, region_of_interest, specialization) пришлось написать кастомный тег
для темплейтов, находящийся в каталоге приложения sample/templatetags custom_filters.py (т.к. к моему удивлению
"магическая" функция get_FOO_display напрочь отказалась работать и отображать какие-либо данные из этих полей в принципе):

    from django import template
    
    register = template.Library()
    
    
    @register.filter(name='get_display')
    def get_display(value, arg):
        return dict(arg).get(value, value)

Благодаря этому тегу отображение человекопонятных значений кортежей вышеописанных трех селектов стало правильно
отрабатывать.

*2.2.1 Главная страница*

Во первых, стоить отметить, что для унификации общего стиля сайта все темплейты строятся на базе одного - base.html, 
верстка которого будет представлена:

    <!DOCTYPE html>
    <html lang="ru">
    {% load static %}
    <head>
        <link rel="icon" href="{% static 'favicon.ico' %}">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        {% block title %}
        {% endblock %}
        <link rel="stylesheet" href="{% static 'sample/styles.css' %}">
    </head>
    <body>
        <header>
            <div class="container">
                <div class="header-top">
                    <h1>Radiology Sample</h1>
                    <div class="register-container">
                        <ul>
                            {% if user.is_authenticated %}
                                <li><a href="/api/v1/auth/logout">Выйти</a></li>
                            {% else %}
                                <li><a href="/api/v1/registration">Регистрация</a> </li>
                                <li><a href="/api/v1/auth/login">Войти</a> </li>
                            {% endif %}
                        </ul>
                    </div>
                </div>
                <div class="header-bottom">
                    <nav>
                        <ul>
                            <li><a href="/">Главная</a></li>
                            <li><a href="/api/v1/sample/get_all_samples">Все описания</a></li>
                            <li><a href="/api/v1/sample/add_sample">Добавить описание</a></li>
                        </ul>
                    </nav>
    
                </div>
            </div>
        </header>
    
        <main class="container">
            {% block content %}
            {% endblock %}
        </main>
    
        <footer>
            <div class="container">
                <p>2023 Radiology Sample</p>
            </div>
        </footer>
    </body>
    </html>

Давайте разберем его содержимое:
Начало и head мало чем примечательны, в них через шаблонизатор django идет загрузка static, затем прокидывается путь
до favicon.ico а также путь до таблицы стилей. Также внутри head'е находится {% block title %}, через который из
остальных темплейтов задается название, идущее во вкладку страницы.
Далее открывается body, в его header'е в первом контейнере расположено название сайта вместе с вложенным контейнером для
кнопок Регистрация/Войти/Выйти c условием прописанным через шаблонизатор django, которое содержит следующую логику:
если пользователь не аворизован - он увидит кнопки Регистрация или Войти, но если пользователь уже авторизован - ему
будет доступна только кнопка Выйти.
Данные кнопки, естественно, отвечают за регистрацию пользователя, login и logout функции соответственно.
Далее располагается второй контейнер header'а, в котором в теге <nav> находятся навигационные кнопки, переводящие
пользователя по основным страницам сайта Главная, Все описания, Добавить описание.
После header'а следует main, в котором и расположен основной контент каждой страницы благодаря вставке {% block content%}
через джанго шаблонизатор.
И в конце в footer'е расположен один контейнер с названием сайта.

Главная страница не многим дополняет base.html, в ней имеется только title для {% block title %} и приветственный h2
заголовок для {% block content %}

    {% extends "sample/base.html" %}
    {% block title %}
        <title>Главная</title>
    {% endblock %}
    {% block content %}
        <h2 class="centered-text">Это главная страница сайта Radiology Sample. <br> Используйте меню для навигации.</h2>
    {% endblock %}

Вот визуальное представление главной страницы сайта:

![Главная страница сайта](/images/image_1.png)

*2.2.2 Списочная страница описаний*

Здесь пользователи видят список всех описаний с отражением всех их полей (кроме текста описания), по всем полям можно 
осуществлять сортировку в порядке убывания и возрастания, доступна фильтрация по полям "Модальность исследования", 
"Зона интереса", "Специализация", а также добавлена возможность поиска по названию описания.

Рассмотрим ее верстку:

    {% extends "sample/base.html" %}
    {% load custom_filters %}
    {% block title %}
        <title>Все описания</title>
    {% endblock %}
    {% block content %}
        <div class="container">
            <div class="filter-form-container">
                <form method="get" action="." class="form-actions">
                    <input type="text" name="title_search" placeholder="Поиск по названию">
                    <select name="modality_filter">
                        <option value="">-- Выберите модальность --</option>
                        {% for code, name in MODALITY_CHOICES %}
                            <option value="{{ code }}">{{ name }}</option>
                        {% endfor %}
                    </select>
                    <select name="region_of_interest_filter">
                        <option value="">-- Выберите зону интереса --</option>
                        {% for code, name in REGION_OF_INTEREST_CHOICES %}
                            <option value="{{ code }}">{{ name }}</option>
                        {% endfor %}
                    </select>
                    <select name="specialization_filter">
                        <option value="">-- Выберите специализацию --</option>
                        {% for code, name in SPECIALIZATION_CHOICES %}
                            <option value="{{ code }}">{{ name }}</option>
                        {% endfor %}
                    </select>
                    <input type="submit" value="Фильтровать">
                </form>
            </div>
            <h2 class="centered-text">Список описаний</h2>
            <table class="sample-table">
                <thead>
                    <tr>
                        <th>
                            Номер
                            {% if ordering == "id" %}
                                <a href="?ordering=-id">⬇️</a>
                            {% elif ordering == "-id" %}
                                <a href="?ordering=id">⬆️</a>
                            {% else %}
                                <a href="?ordering=id">↕️</a>
                            {% endif %}
                        </th>
                        <th>
                            Заголовок описания
                            {% if ordering == "title" %}
                                <a href="?ordering=-title">⬇️</a>
                            {% elif ordering == "-title" %}
                                <a href="?ordering=title">⬆️</a>
                            {% else %}
                                <a href="?ordering=title">↕️</a>
                            {% endif %}
                        </th>
                        <th>
                            Дата создания
                            {% if ordering == "datetime_of_creation" %}
                                <a href="?ordering=-datetime_of_creation">⬇️</a>
                            {% elif ordering == "-datetime_of_creation" %}
                                <a href="?ordering=datetime_of_creation">⬆️</a>
                            {% else %}
                                <a href="?ordering=datetime_of_creation">↕️</a>
                            {% endif %}
                        </th>
                        <th>
                            Дата изменения
                            {% if ordering == "datetime_of_change" %}
                                <a href="?ordering=-datetime_of_change">⬇️</a>
                            {% elif ordering == "-datetime_of_change" %}
                                <a href="?ordering=datetime_of_change">⬆️</a>
                            {% else %}
                                <a href="?ordering=datetime_of_change">↕️</a>
                            {% endif %}
                        </th>
                        <th>
                            Модальность исследования
                            {% if ordering == "modality" %}
                                <a href="?ordering=-modality">⬇️</a>
                            {% elif ordering == "-modality" %}
                                <a href="?ordering=modality">⬆️</a>
                            {% else %}
                                <a href="?ordering=modality">↕️</a>
                            {% endif %}
                        </th>
                        <th>
                            Зона исследования
                            {% if ordering == "region_of_interest" %}
                                <a href="?ordering=-region_of_interest">⬇️</a>
                            {% elif ordering == "-region_of_interest" %}
                                <a href="?ordering=region_of_interest">⬆️</a>
                            {% else %}
                                <a href="?ordering=region_of_interest">↕️</a>
                            {% endif %}
                        </th>
                        <th>
                            Специализация
                            {% if ordering == "specialization" %}
                                <a href="?ordering=-specialization">⬇️</a>
                            {% elif ordering == "-specialization" %}
                                <a href="?ordering=specialization">⬆️</a>
                            {% else %}
                                <a href="?ordering=specialization">↕️</a>
                            {% endif %}
                        </th>
                    </tr>
                </thead>
                <tbody>
                    {% for sample in samples %}
                        <tr>
                            <td>{{ sample.id }}</td>
                            <td>
                                <a href="/api/v1/sample/{{ sample.id }}/get_defined_sample">{{ sample.title }}</a>
                            </td>
                            <td>{{ sample.datetime_of_creation }}</td>
                            <td>{{ sample.datetime_of_change }}</td>
                            <td>{{ sample.modality|get_display:MODALITY_CHOICES }}</td>
                            <td>{{ sample.region_of_interest|get_display:REGION_OF_INTEREST_CHOICES }}</td>
                            <td>{{ sample.specialization|get_display:SPECIALIZATION_CHOICES }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    {% endblock %}

Как я уже говорил выше, для реализации адекватного отображения человекопонятного представления селектов полей modality,
region_of_interest, specialization мне пришлось написать кастомный тег, вместо неработающей "магической" функции
get_FOO_display. Он и загружается через шаблонизатор благодаря {% load custom_filters %}.
Далее у нас представлен {% block content %}, в котором все начинается с фильтров по вышеописанным трем полям, где и
применен данный тег, который при получении значения трех селектов из базы данных переводит их в человекопонятный вид.
При выборе в этой форме фильтрации каких либо значений и нажатии кнопки фильтровать, данное значение передается на backend,
где и происходит фильтрация всех экземпляров шаблонов описаний по полученным в этой форме с frontend'а параметрам.
Также обстоят дела и с полем поиска.
Далее с помощью тегов <table> а также внутри нее тегов <thead> и <tbody> я формирую таблицу, в которую передаются с
backend'а значения полей для каждого экземпляра шаблона описания через цикл {% for sample in samples %}.
Также можно заметить, что данные значения при нажатии на кнопки рядом с заголовками столбцов этой таблицы можно
фильтровать как в порядке возрастания, так и в порядке убывания. Фильтрация со стороны backend'ф была продемонстрирована
ранее.

Таким образом, внешний вид данной страницы выглядит так:

![Списочная страница шаблонов описаний](/images/image_2.png)

*2.2.3 Страница конкретного описания (деталка описания)*

При нажатии на конкретное описание пользователь переходит на страницу, где представлена подробная информация об этом 
исследовании (с полями "Заголовок" и "Текст описания"), а также возможность скопировать текст описания в буфер обмена 
при помощи соответствующей кнопки.

Рассмотрим верстку данной страницы:

    {% extends "sample/base.html" %}
    {% block title %}
        <title>Описание: {{ defined_sample.title }}</title>
    {% endblock %}
    {% block content %}
        <h2 class="centered-text">{{ defined_sample.title }}</h2>
        <div class="description__container">
            <p class="description__text" id="descriptionText">{{ defined_sample.text }}</p>
        </div>
        <div class="center-container">
            <button onclick="copyToClipboard()">Копировать текст</button>
        </div>
        <div id="customModal" class="modal">
            <div class="modal-content">
                <span class="close-button">&times;</span>
                <p class="modal-text"></p>
            </div>
        </div>
        <script>
            var modal = document.getElementById('customModal');
            var closeButton = document.querySelector('.close-button');
            var modalText = document.querySelector('.modal-text');
            closeButton.onclick = function() {
                modal.style.display = "none";
            }
            window.onclick = function(event) {
                if (event.target == modal) {
                    modal.style.display = "none";
                }
            }
            function showModal(message) {
                modalText.innerHTML = message;
                modal.style.display = "block";
            }
            async function copyToClipboard() {
                try {
                    const textToCopy = document.getElementById('descriptionText').innerText;
                    await navigator.clipboard.writeText(textToCopy);
                    showModal("Текст скопирован в буфер обмена!");
                } catch (err) {
                    showModal("Не удалось скопировать текст:<br>" + err);
                }
            }
        </script>
    {% endblock %}

Само отображение полей заголовка и текста описания не представляет из себя ничего интересного и новго. Тем не менее, 
для удобства пользователей я сделал кнопку "Копировать текст", чтобы при ее нажатии текст автоматически копировался
в буфер обмена. Взглянем на ее реализацию:
В теге <button> было задан параметр onclick="copyToClipboard()", который при нажатии кнопки запускает функцию
copyToClipboard(). Она описана ниже в теге <script> - мы получаем вначале текст, который нужно скопировать, согласно
id="descriptionText", который указан в теге <p>, в который и пробрасывается текст конкретного шаблона описания через
шаблонизатор django. Далее с помощью API JavaScript navigator.clipboard.writeText мы копируем этот текст в буфер обмена.
При успешном копировании пользователю показывается модальное окно с текстом об успешном копировании в буфер обмена, 
при неудаче - отображается аналогичное модальное окно с текстом ошибки, которая к ней привела.

Здесь представлен внешний вид страницы и модального окна:

![Детальная страница шаблона описания](/images/image_3_1.png)
![Модальное окно на странице шаблона описания](/images/image_3_2.png)

*2.2.3 Страница добавления нового описания*

Данная страница представлена формой для ввода информации о новом описании со всеми соответствующими полями этой модели,
при успешном заполнении всех полей и создании нового описания пользователь переходит на страницу, которая его 
уведомляет об успехе и предлагает добавить еще одно описание или перейти на главную страницу.

Рассмотрим ее верстку:

    {% extends "sample/base.html" %}
    {% block title %}
        <title>Добавить описание</title>
    {% endblock %}
    {% block content %}
    <div class="container form-container">
        <h2>Добавление нового описания</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <div class="form-actions">
                <button type="submit">Добавить</button>
            </div>
        </form>
    </div>
    {% endblock %}

Данная страница представляет из себя {% block content %}, в который помещен контейнер с методом {{ form.as_p }}
шаблонизатора django, который предлагает удобное представление формы в виде абзацев, который упрощает создание форм.
При успешном заполнении всех необходимых полей формы и прохождения ей всех стандартных валидаций django пользователя
переносит на страницу, которая сообщает об успешном создании нового экземпляра модели шаблона описания и предлагает две
кнопки: для возвращения на главную страницу сайта и для добавления еще одного шаблона описания. Вот верстка этой страницы,
думаю, что подробного разъяснения она не требует:

    {% extends "sample/base.html" %}
    {% block title %}
        <title>{{ message }}</title>
    {% endblock %}
    {% block content %}
    <div class="container">
        <div class="success-message">
            <h2>{{ message }}</h2>
            <p>Дальнейшие действия:</p>
            <a href="/api/v1/sample/add_sample">Добавить еще одно описание</a>
            или 
            <a href="/">Вернуться на главную</a>
        </div>
    </div>
    {% endblock %}

Внешний вид этих страниц представлен ниже:

![Страница добавления шаблона описания](/images/image_4_1.png)
![Успех на странице добавления шаблона описания](/images/image_4_2.png)

*2.2.4 Страницы регистрации и login*

Также были созданы темплейт для страницы регистрации пользователя и кастомный темплейт для страницы login (drf предоставляет
свой вариант из коробки, тем не менее, для поддержания общего стиля сайта было решено сделать кастом):

Рассмотрим темплейт формы регистрации:

    {% extends "sample/base.html" %}
    {% block title %}
        <title>Регистрация</title>
    {% endblock %}
    {% block content %}
    <div class="container form-container">
        <h2>Регистрация</h2>
        <form method="post">
            {% csrf_token %}
            {{ form.as_p }}
            <div class="form-actions">
                <button type="submit">Зарегистрироваться</button>
            </div>
        </form>
    </div>
    {% endblock %}

В данном случае его реализация довольно аналогична с темплейтом формы создания нового экземпляра модели шаблона описания.

Ниже представлена верстка страницы login:

    {% extends "sample/base.html" %}
    {% block title %}
        <title>Войти</title>
    {% endblock %}
    {% block content %}
    <div class="container form-container">
        <h2>Войти</h2>
        <form method="post">
            {% csrf_token %}
            <p>
                <label for="id_username">Имя пользователя:</label>
                <input type="text" name="username" id="id_username" required>
            </p>
            <p>
                <label for="id_password">Пароль:</label>
                <input type="password" name="password" id="id_password" required>
            </p>
            <div class="form-actions">
                <button type="submit">Войти</button>
            </div>
        </form>
    </div>
    {% endblock %}

Она также напоминает предыдущую, за тем исключением, что у нее нет своей собственной формы на backend'е, поэтому
здесь не получится использовать {{ form.as_p }}, вместо него здесь были созданы обычные абзацы с полями для ввода данных.

Вот внешнее представление описанных выше страниц:

![Страница регистрации пользователя](/images/image_5_1.png)
![Страница login](/images/image_5_2.png)

*2.2.5 Таблица стилей*

Ниже будет представлена основная таблица стилей, которые использовались для верстки сайта (также, некоторые кастомные
формы содержат стили отдельно внутри):

    html, body {
        height: 100%;
        margin: 0;
    }
    
    body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f5f5f5;
        color: #333;
        display: flex;
        flex-direction: column;
    }
    
    .container {
        width: 90%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }
    
    header {
        background-color: #333;
        color: #fff;
        padding: 10px 0;
        text-align: center;
    }
    
    header .container {
        display: flex;
        flex-direction: column;
    }
    
    .header-bottom {
        display: flex;
        justify-content: space-between;
        align-items: center;
        width: 100%;
    }
    
    header h1 {
        margin: 0;
    }
    
    nav {
        display: flex;
        justify-content: center;
        flex-grow: 1;
    }
    
    nav ul {
        list-style-type: none;
        padding: 0;
        margin: 20px 0;
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    
    nav ul li {
        margin: 0 10px;
    }
    
    nav ul li a {
        text-decoration: none;
        color: #fff;
        padding: 5px 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    
    nav ul li a:hover {
        background-color: #555;
    }
    
    main {
        padding: 20px;
        flex: 1 0 auto;
    }
    
    footer {
        background-color: #333;
        color: #fff;
        text-align: center;
        padding: 10px 0;
        margin-top: 20px;
        flex-shrink: 0;
    }
    
    .sample-table {
        width: 100%;
        border-collapse: collapse;
    }
    
    .sample-table th, .sample-table td {
        border: 1px solid #ccc;
        padding: 10px;
        text-align: center;
    }
    
    .sample-table th {
        background-color: #e6e6e6;
        text-align: center;
    }
    
    .centered-text {
        text-align: center;
    }
    
    .description__text {
        width:900px;
        text-align:center;
    }
    
    .description__container {
        display: flex;
        width: 100%;
        justify-content: center;
        line-height: 150%;
        margin-bottom: 10px;
    }
    
    .modal {
        display: none;
        position: fixed;
        z-index: 1;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        overflow: auto;
        background-color: rgba(0,0,0,0.7);
    }
    
    .modal-content {
        position: relative;
        background-color: #fefefe;
        margin: 15% auto;
        padding: 20px;
        border: 1px solid #888;
        width: 35%;
        text-align: center;
    }
    
    .close-button {
        color: #aaa;
        float: right;
        font-size: 28px;
        font-weight: bold;
        cursor: pointer;
    }
    
    .close-button:hover,
    .close-button:focus {
        color: black;
        text-decoration: none;
        cursor: pointer;
    }
    
    .filter-form-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    
    .register-container ul {
        list-style-type: none;
        padding: 0;
        margin: 20px 0;
        display: flex;
        justify-content: center;
        gap: 10px;
    }
    
    .register-container ul li {
        margin: 0 10px;
    }
    
    .register-container ul li a {
        text-decoration: none;
        color: #fff;
        padding: 5px 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    
    .register-container ul li a:hover {
        background-color: #555;
    }
    
    .header-top {
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        align-items: center;
        width: 100%;
    }
    
    h1 {
        grid-column: 2;
        text-align: center;
    }
    
    .register-container {
        grid-column: 3;
        justify-self: end;
    }
    
    .center-container {
        display: flex;
        justify-content: center;
    }

*2.3 Безопасность веб-платформы*

*2.3.1 Аутентификация и авторизация*

Система авторизации разделяет пользователей на несколько уровней доступа: авторизованные (обычные) пользователи и 
администраторы. Также пользователям доступна самостоятельная регистрация на платформе, login и logout.
Как я уже описывал выше, на backend'е реализованы разрешения на просмотр всех страниц кроме главной только для 
авторизованных пользователей через permission_classes = [IsAuthenticated]. В дальнейшем, при доработке проекта можно
реализовать систему регистрации с подтверждением email. А для использования системы в условиях больниц для сохранения
приватности и врачебной тайны возможно реализовать доступ к ней только в локальной сети больницы и убрать возможность
самостоятельной регистрации пользователей - таким образом для работников аккаунты будут создаваться системным администратором
через доступ в административную панель сайта и ручного создания аккаунта для каждого работника, которому необходим
доступ к системе.

*2.4 Тестирование веб-платформы*

После завершения разработки платформы было проведено функциональное тестирование. Основные API платформы покрыты 
unit-тестами (как положительными так и отрицательными). Выше, при описании backend части платформы, был приведен их
код с разъяснениями.

---

**Глава 3: Оценка и обоснование ценности проекта**

*3.1 Полезность платформы для медицинского сообщества*

*3.1.1 Централизованное хранилище данных*

В современном медицинском мире информация становится ключевым ресурсом. Веб-платформа, предлагая централизованное 
хранилище для рентгеновских исследований, отвечает на вызовы, связанные с эффективностью хранения, доступом и передачей 
данных. Когда информация разбросана по различным источникам или учреждениям, это не только затрудняет доступ к ней, но 
и увеличивает вероятность ошибок и недоразумений. Эффективное централизованное хранилище позволяет специалистам надежно 
хранить данные, делать быстрый запрос и получать ответы в режиме реального времени.

Более того, платформа снижает риски, связанные с утратой или повреждением данных, предоставляя надежные резервные копии 
и системы безопасности. Для новых медицинских работников такая платформа становится инструментом быстрого старта: они 
могут погрузиться в архивы, изучать исторические данные, а также ознакомиться с текущими практиками и стандартами.

*3.1.2 Обмен опытом*

Медицина - это не статичная наука. Она постоянно развивается благодаря исследованиям, инновациям и, что немаловажно, 
обмену опытом между специалистами. Глобальная платформа предлагает уникальную возможность для медицинских экспертов из 
разных уголков мира объединять свои знания и навыки.

Такой обмен может осуществляться в различных форматах: от кратких консультаций до подробных дискуссий о сложных 
клинических случаях. Когда врач из Европы может обсудить сложный диагностический случай с коллегой из Азии, это не 
только улучшает исход для конкретного пациента, но и расширяет горизонты обоих специалистов, позволяя видеть проблему 
под разными углами.

Кроме того, обмен опытом может стать катализатором для новых исследований и разработок, так как объединение усилий 
и ресурсов ученых и практиков из разных стран может привести к созданию новых методов диагностики, лечения и 
реабилитации пациентов.

*3.2 Экономическая ценность*

*3.2.1 Эффективность использования ресурсов*

В современном мире, где ограниченные ресурсы и бюджеты часто становятся препятствием для масштабирования и инноваций, 
централизованное хранилище представляет собой оптимальное решение для многих медицинских учреждений. Когда каждое 
учреждение пытается создать и поддерживать свою собственную систему, это может привести к значительным финансовым и 
временным издержкам.

Централизованная платформа позволяет избегать избыточных затрат на разработку, обновление и поддержку системы. Она 
также уменьшает риск технических ошибок или сбоев, которые могут возникнуть при многократном дублировании системы. Т
аким образом, учреждения могут перераспределить свои ресурсы на другие важные аспекты медицинской деятельности, такие 
как исследования или обучение.

*3.2.2 Потенциальный коммерческий интерес*

С ростом числа пользователей и накоплением данных платформа становится ценным активом не только для медицинских 
специалистов, но и для коммерческих организаций. Медицинские учреждения, исследовательские лаборатории и 
фармацевтические компании могут видеть в платформе потенциальный источник ценных данных, которые можно использовать для 
аналитики, научных исследований или даже создания новых продуктов.

Для фармацевтической отрасли, например, доступ к реальным данным пациентов может помочь в разработке новых препаратов, 
оптимизации клинических испытаний или даже в целевом маркетинге. Платформа может стать местом для проведения рекламных 
кампаний, партнерств или спонсорства.

В долгосрочной перспективе, платформа, обладая таким количеством данных и аналитическим потенциалом, может стать не 
только центром медицинского обмена опытом, но и коммерческим хабом, предоставляя возможности для множества 
стейкхолдеров в медицинской сфере.

*3.3 Образовательная ценность*

*3.3.1 Для студентов*

В цифровую эпоху студентам медицинских специальностей необходим доступ к актуальным и реальным данным для обогащения 
своего учебного опыта. Платформа становится не просто источником информации, но и виртуальной лабораторией, где можно 
проводить "эксперименты" в безопасной среде. Студенты могут анализировать реальные случаи, обсуждать их со своими 
коллегами, пробовать различные методы диагностики и лечения, а также получать обратную связь от опытных специалистов.

Такой подход помогает студентам развивать свою аналитическую способность, лучше понимать практические аспекты профессии 
и формировать профессиональный взгляд на медицину. Это также подготавливает их к реальной практике, делая переход от 
теории к практике более плавным.

*3.3.2 Для преподавателей*

Для преподавателей платформа становится настоящей "золотой жилой" образовательного контента. Она предоставляет 
возможность не только показывать реальные примеры пациентов, но и создавать интерактивные учебные модули, в которых 
студенты могут принимать решения и видеть их последствия.

Преподаватели могут использовать платформу для создания групповых заданий, где студенты будут работать над реальными 
кейсами, анализировать информацию, предлагать методы лечения и обсуждать их с коллегами. Такой подход стимулирует 
критическое мышление, развивает навыки командной работы и повышает мотивацию к обучению.

Кроме того, платформа может служить местом для профессионального развития преподавателей. Они могут обмениваться 
опытом с коллегами из других учебных заведений, участвовать в семинарах или вебинарах, а также получать доступ к 
новейшим исследованиям и методикам обучения.

**Глава 4: Выводы по работе**

**Глава 5: Список использованной литературы (источников информации)**

При написании данной работы была использована техническая документация:
- https://docs.djangoproject.com/en/4.2/
- https://www.django-rest-framework.org/
- https://drf-yasg.readthedocs.io/en/stable/
- https://doka.guide/
- https://djangodoc.ru/3.1/ref/templates/language/