from django.db import models
import random
import string


class MiniURL(models.Model):
    url = models.URLField(verbose_name="URL to minify", unique=True)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True, 
                                verbose_name="Created At")
    pseudo = models.CharField(max_length=255, blank=True, null=True)
    nb_access = models.IntegerField(default=0, 
                                   verbose_name="Access to URL")

    def __str__(self):
        return "[{0}] {1}".format(self.code, self.url)

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.generate(6)

        super(MiniURL, self).save(*args, **kwargs)

    def generate(self, nb_caracteres):
        caracteres = string.ascii_letters + string.digits
        aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]

        self.code = ''.join(aleatoire)

    class Meta:
        verbose_name = "Mini URL"
        verbose_name_plural = "Minis URL"


def renommage(instance, nom):
    nom_fichier = os.path.splitext(nom)[0] # on retire l'extension
    ext = os.path.splitext(nom)[1]
    return "photos/{}-{}{}".format(instance.id, nom_fichier, ext)

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    contenu = models.TextField(null=True)
    slug = models.SlugField(max_length=100)
    date = models.DateTimeField(auto_now_add=True, auto_now=False, 
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie')
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.titre
    
class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
    
class Moteur(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom

class Voiture(models.Model):
    nom = models.CharField(max_length=25)
    moteur = models.OneToOneField(Moteur)

    def __str__(self):
        return self.nom
    
class Produit(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Vendeur(models.Model):
    nom = models.CharField(max_length=30)
    produits = models.ManyToManyField(Produit, through='Offre')
    
    def __str__(self):
        return self.nom

class Offre(models.Model):
    prix = models.IntegerField()
    produit = models.ForeignKey(Produit)
    vendeur = models.ForeignKey(Vendeur)

    def __str__(self):
        return "{0} vendu par {1}".format(self.produit, self.vendeur)

class Contact(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.TextField()
    photo = models.ImageField(upload_to=renommage)
    
    def __str__(self):
           return self.nom

class Eleve(models.Model):
    nom = models.CharField(max_length=31)
    moyenne = models.IntegerField(default=10)

    def __str__(self):
        return "Élève {0} ({1}/20 de moyenne)".format(self.nom, self.moyenne)

class Cours(models.Model):
    nom = models.CharField(max_length=31)
    eleves = models.ManyToManyField(Eleve)

    def __str__(self):
        return self.nom

class Document(models.Model):
    titre = models.CharField(max_length=255)
    date_ajout = models.DateTimeField(auto_now_add=True, 
                                      verbose_name="Date d'ajout du document")
    auteur = models.CharField(max_length=255, null=True, blank=True)
    
    class Meta:
        abstract = True
    
class Article(Document):
    contenu = models.TextField()  
    
class Image(Document):
    image = models.ImageField(upload_to="images")