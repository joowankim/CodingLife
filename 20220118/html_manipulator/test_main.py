from bs4 import BeautifulSoup


def test_main():
    template = "template.html"
    manipulated = "manipulated.html"

    with open(template, "r") as f:
        soup = BeautifulSoup(f, features="html.parser")

        # find p with tag name
        assert soup.p.string == "p tag"

        # find div with class name
        assert soup.select_one(".div-class").string == "div class"

        # create new tag
        tr = soup.new_tag("tr")

        td_one = soup.new_tag("td")
        td_one.string = "table td one"
        tr.append(td_one)

        td_two = soup.new_tag("td")
        td_two.string = "table td two"
        tr.append(td_two)

        td_three = soup.new_tag("td")
        td_three.string = "table td three"
        tr.append(td_three)

        # add table row with BeautifulSoup
        soup.tbody.append(tr)

    # write manipulated html
    with open(manipulated, "w") as f:
        f.write(str(soup))

    # read manipulated html
    with open(manipulated, "r") as f:
        manipulated_html = BeautifulSoup(f, features="html.parser")

        assert manipulated_html.tbody.findChild() == tr
