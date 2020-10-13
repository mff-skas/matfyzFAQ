import csv

def get_config():
  title = "Matfyz FAQ"
  subtitle = "To, na co jste se nás již nejednou ptali"

  # Usage: ("Nadpis sekce", "unikatni identifikatro (bude slouzit i jako predpona pro nedefinovana jmena linku; nesmi obsahovat podtrzitko)", "cesta k souboru s otazkami");
  sections = [
    ("COVID-19 dotazy", "covid", "questions_answers/covid_dotazy.csv"),
    ("Obecné dotazy", "obecne", "questions_answers/obecne_dotazy.csv"),
    ("Fyzikální dotazy","fyzikalni","questions_answers/fyzikalni_dotazy.csv"),
    ("Informatické dotazy","informaticke","questions_answers/informaticke_dotazy.csv"),
    ("Matematické dotazy","matematicke","questions_answers/matematicke_dotazy.csv")
  ]

  return (title, subtitle, sections)

def print_head(title, subtitle):
  head = f'''\
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="cs" lang="cs">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <meta property="og:image" content="./faq_icon.png" />
  <meta property="og:image:type" content="image/png" />
  <meta property="og:image:width" content="400" />
  <meta property="og:image:height" content="400" />
  <meta property="og:description" content="{subtitle}" />
  <title>{title}</title>
  <base target="_parent">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="assets/web/assets/mobirise-icons/mobirise-icons.css" type="text/css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css" type="text/css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-grid.min.css" type="text/css">
  <link rel="stylesheet" href="assets/bootstrap/css/bootstrap-reboot.min.css" type="text/css">
  <link rel="stylesheet" href="assets/theme/css/style.css" type="text/css">
  <link rel="stylesheet" href="assets/mobirise/css/mbr-additional.css" type="text/css">
  <link rel="shortcut icon" type="image/x-icon" href="/favicon.ico"/>
  <link rel="icon" type="image/x-icon" href="/favicon.ico"/>
<style>
.mbr-fonts-style{{line-height: 1.5;}}
</style>'''

  script = r'''
<script>
    function gen_mail_to_link(lhs,rhs,subject,classes) {
        document.write("<a href=\"mailto");
        document.write(":" + lhs + "@");
        document.write(rhs + "?subject=" + subject + "\" class=\"" + classes +"\">" + lhs + "@" + rhs + "<\/a>");
    }

    function scroll_to_hash(){
        var hash = window.location.hash.substr(1).split("_").pop();
        if (hash)
        {
            location.href = "#";
            location.href = "#dotaz_"+ hash;
            document.getElementById("question_"+hash).classList.add("mbri-arrow-up");
            document.getElementById("question_"+hash).classList.remove("mbri-arrow-down");
            document.getElementById("btn_"+hash).classList.remove("collapsed");
            document.getElementById("btn_"+hash).setAttribute("aria-expanded", "true");
            document.getElementById(hash).classList.add("show");
        }
    }

    function copyToClipboard(text) {
        window.prompt("Zkopíruj si odkaz a pošli ho tazateli!", window.location.protocol + "//" + window.location.hostname + window.location.pathname + text)
    }

</script>'''

  header = f'''
</head>
<body onload="scroll_to_hash();">
<section class="header11 cid-qv5BLEQHXO" id="header" data-rv-view="2085">
    <div class="container align-left">
        <div class="media-container-column mbr-white col-md-12">
            <h1 class="mbr-section-title py-3 mbr-fonts-style display-1">{title}</h1>
            <h3 class="mbr-section-title py-3 mbr-fonts-style display-2">{subtitle}</h3>
        </div>
    </div>
</section>'''

  print(head)
  print(script)
  print(header)

def print_section(title, id, path):
  header = f'''\
    <section class="toggle1 cid-qv5Aju6kt2" id="dotaz_{id}" data-rv-view="2091">
      <div class="container" role="tablist">
            <div class="media-container-row">
                <div class="col-12 col-md-12">
                    <div class="section-head text-center space30">
                       <h2 class="mbr-section-title pb-5 mbr-fonts-style display-2">{title}</h2>
                    </div>
                    <div class="clearfix"></div>
                    <div id="bootstrap-toggle-{id}" class="toggle-panel accordionStyles tab-content"><br />'''
  print(header)

  with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    next(csvreader)

    i = 1
    for row in csvreader:
      question, answer, link = row
      link = link if link != "" else f"{id}-{i}"

      body = f'''\
                <div class="card">
                    <div class="card-header" role="tab" id="dotaz_{link}">
                        <a role="button" class="collapsed panel-title text-black" data-toggle="collapse" data-parent="#accordion" data-core="" href="#{link}" id="btn_{link}" aria-expanded="false" aria-controls="{link}">
                            <h4 class="mbr-fonts-style display-6">
                                <span class="sign mbr-iconfont mbri-arrow-down inactive" id="question_{link}"></span>{question}
                            </h4>
                        </a>
                    </div>
                    <div id="{link}" class="panel-collapse noScroll collapse" role="tabpanel" aria-labelledby="dotaz_{link}">
                        <div class="panel-body px-4 pt-4">
                            <p class="mbr-fonts-style panel-text display-7">{answer}
                        </div>
                        <span class="pb-4 mbri-link-chain" style="float: right;padding-bottom:5px;" onclick="copyToClipboard(\'#{link}\')" title="odkaz"></span>
                    </div>
                </div> '''
      print(body)
      i += 1

  footer = '''\
                  </div>
                </div>
            </div>
        </div>
</section>'''
  print(footer)

def print_sections(sections):
  for section in sections:
    title, id, path = section
    print_section(title, id, path)

def print_footer():
  footer = f'''\
<section class="header11 cid-qv5BLEQHXO" id="disclaimer" data-rv-view="2085">
    <div class="container align-center">
        <div class="media-container-column mbr-white col-md-12">

            <h4 class="py-4 mbr-fonts-style" style="font-size: 1.5em;">Máš pocit, že tu není všechno? Zkus se zeptat spolužáků nebo nám napiš na e-mail <script>gen_mail_to_link('faq','matfyz.cz','[Matfyz FAQ]', 'text-white');</script>.</h4>
        </div>
    </div>
</section>

<section class="cid-qvLq468qgu" id="fakefooter" data-rv-view="2128" />
<br />
<br />
<br />
<section class="cid-qvLq468qgu" id="footer" data-rv-view="2128" style="position:absolute; bottom:0%; width:100%">
    <div class="container">
        <div class="media-container-row align-center mbr-white">
            <div class="col-12">
                <h6 class="mbr-text mb-0 mbr-fonts-style display-7" style="font-weight:normal;">
                    Authors: <a href="http://pobdr.matfyz.cz" class="text-white">Pavel Obdržálek</a>, <a href="http://www.ms.mff.cuni.cz/~yaghoboa/" class="text-white">Anna Yaghobová</a>, Míra Štochel, <a href="https://petrroll.cz" class="text-white">Petr Houška</a>, <a href="https://vilda.net" class="text-white">Vilém Zouhar</a>, Petra Hoffmannová, Peter Korcsok, Honza Hrabovský, Vojtěch Švandelík a spousta dotazovatelů z řad studentů…
                </h6>
                Tento web máme na <a href="https://github.com/mff-skas/matfyzFAQ" class="text-white">GitHubu</a>!
                <h6 class="mbr-text mb-0 mbr-fonts-style display-7" style="font-weight:normal;">
                    &copy; Theme copyright: <a href="https://mobirise.com/bootstrap-template/" class="text-white">Free Bootstrap Templates</a>, edited by <a href="http://pobdr.matfyz.cz" class="text-white">Pavel Obdržálek</a>
                </h6>
            </div>
        </div>
    </div>
</section>

  <script src="assets/web/assets/jquery/jquery.min.js"></script>
  <script src="assets/popper/popper.min.js"></script>
  <script src="assets/bootstrap/js/bootstrap.min.js"></script>
  <script src="assets/theme/js/script.js"></script>
</body>
</html> '''
  print(footer)

if __name__ == '__main__':
  title, subtitle, sections = get_config()

  print_head(title, subtitle)
  print_sections(sections)
  print_footer()
