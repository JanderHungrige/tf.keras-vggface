from setuptools import setup, find_packages
exec(open('keras_vggface_TF/version.py').read())
setup(
    name='keras_vggface_TF',
    version=__version__,
    description='VGGFace implementation with tf.keras framework, based on rcmalli',
    url='https://github.com/JanderHungrige/tf.keras-vggface',
    author='Jan Werth',
    author_email="werth.jan@gmail.com",
    license='MIT',
    keywords=['tf.keras', 'vggface', 'deeplearning'],
    packages=find_packages(exclude=["tools", "training", "temp", "test", "data", "visualize","image",".venv",".github"]),
    zip_safe=False,
    install_requires=[
        'numpy>=1.9.1', 'scipy>=0.14', 'h5py', 'pillow', 'tensorflow>=1.15.3',
        'six>=1.9.0', 'pyyaml','tensorboard >=1.15.3'
    ],
    extras_require={
        "tf": ["tensorflow>=1.15.3"],
        "tf_gpu": ["tensorflow-gpu>=1.15.3"],
    })
