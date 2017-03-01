# anubad-web
this is just a web-interface for popular-anubad

for mvp it is created using bottle, for simplicity

for now it is by no means a replacement for anubad desktop version.
lets see what happens.

### Contents
- [Use](#use)
- [Installation](#installation)
- [Versioning](#versioning)
- [Faq](#faq)
- [Contribute](#contribute)
- [Release](#release)
- [Todos](#todos)
- [Known issues](#known-issues)
- [License](#gplv3-license)
- [Disclaimer](#disclaimer)

## Use

For web interface use [http://anubad.herokuapp.com/](http://anubad.herokuapp.com/)

For api use [http://anubad.herokuapp.com/api/search?phrase=word](http://anubad.herokuapp.com/api/search?phrase=word)

## Installation

### Requirement
    
> We give you no guarantee that it will run in your development environment. It has been tested in linux with python version 3.5.1 only
    
* git
* python3 (preferrable 3.5)
* [**bottle**](http://bottlepy.org)
* [**plim**](http://plim.readthedocs.io/en/latest/)
    
### Setting up the development environment

1. virtualenv (optional)

    ```bash
        # create virtualenv
        $ virtualenv venv -p /usr/bin/python3 
        
        # activate virtualenv
        source /path/to/virtualenv/bin/activate
    ```
    
2. clone it in your machine and install submodules

    ```bash
        # go to projects directory
        $ cd /path/to/projects
        
        # clone it in your system
        $ git clone https://github.com/foss-np/anubad-web.git
        
        # go to project root directory
        $ cd anubad-web
        
        # init submodules
        $ git submodule init
        
        # update submodules
        $ git submodule update
    ```
    
3. install dependencies

    ```bash
	# For virtualenv based installation
        $ pip install -r requirements.txt
    ```
    ```bash
	# For system wide installation 
        $ sudo pip install -r requirements.txt
    ```
4. configure project 

    ```bash
        # go to anubad submodule
        $ cd libs/anubad
        
        # checkout to a master branch
        # because, we can say anything about experimental branch
        $ git checkout master

        # configure anubad
        $ ./configure
        
        # checkout to a working commit in the experimental branch
        # because most commits in this branch may not be functional
        $ git checkout f7c48cf213e524c6862f996cf1154db69f7c1269
        
    ```
    
5. create and configure **config/anubad_core.cnf**
    
    ```bash
        $ cp config/anubad_core.cnf.sample config/anubad_core.cnf
    ```

    > update your path in anubad for gloss in the file **config/anubad_core.cnf**
      / this line /
      > path = /path/to/anubad-web/libs/anubad/gloss/foss/
   
6. run server

    ```bash
        python run.py
    ```

### Deployment in Heroku

```bash
    # Create a heroku app
    $ heroku apps:create webad

    # push the branch heroku-deploy to master branch in heroku
    git push heroku heroku-deploy:master

    # run an instance of the app
    $ heroku ps:scale web=1

    # open the website
    $ heroku open
```

## Versioning

> to be filled

## FAQ

> Questions list empty till now

## Contribute

> to be filled

## Release

> to be filled

## TODOs

* Port Database from the file
* Look and feel ( that UIUX thing)
* Port all features of desktop anubad
* A lot of things

## Known Issuses

> to be filled

## GPLv3 License
    
    Anubad-web is open source under the version 3 of GNU General Public License (GNU GPLv3) license. See [LICENSE](LICENSE) for details.

## Disclaimer

> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
