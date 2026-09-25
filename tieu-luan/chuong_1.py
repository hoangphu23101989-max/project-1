# -*- coding: utf-8 -*-
"""Chương 1. Cơ sở lý luận về cặp phạm trù bản chất và hiện tượng."""

BLOCKS = [
    ("h1", "CHƯƠNG 1\nCƠ SỞ LÝ LUẬN VỀ CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG",
     "CHƯƠNG 1. CƠ SỞ LÝ LUẬN VỀ CẶP PHẠM TRÙ BẢN CHẤT VÀ HIỆN TƯỢNG"),

    # ------------------------------------------------------------------ 1.1
    ("h2", "1.1. Phạm trù và hệ thống phạm trù của phép biện chứng duy vật"),
    ("h3", "1.1.1. Khái niệm phạm trù"),
    ("p", "Phạm trù là những khái niệm rộng nhất, phản ánh những mặt, những thuộc tính, những mối liên hệ "
          "chung, cơ bản nhất của các sự vật và hiện tượng thuộc một lĩnh vực nhất định [@bgd2021]. Mỗi "
          "khoa học cụ thể có hệ thống phạm trù riêng; chẳng hạn, “liên kết hóa học”, “cơ chế phản ứng”, "
          "“ái lực gắn kết” là các phạm trù của hóa học và hóa sinh, phản ánh các mối liên hệ trong một "
          "lĩnh vực hiện thực xác định. Phạm trù của phép biện chứng duy vật có phạm vi rộng hơn: chúng "
          "phản ánh những mối liên hệ phổ biến nhất, có mặt trong tự nhiên, xã hội và tư duy. Vì vậy, phạm "
          "trù triết học không thay thế phạm trù của khoa học cụ thể, mà đóng vai trò định hướng phương "
          "pháp luận cho việc hình thành và sử dụng các phạm trù ấy [@bgd2015; @bgd2021]."),
    ("p", "Trong lịch sử triết học, vấn đề phạm trù được giải quyết theo những lập trường khác nhau. "
          "Arixtốt là người đầu tiên xây dựng một hệ thống phạm trù tương đối hoàn chỉnh, xem phạm trù là "
          "những thể loại chung nhất của tồn tại và của phát ngôn về tồn tại. I. Cantơ coi phạm trù là "
          "những hình thức tiên nghiệm của giác tính, vốn có trong chủ thể và được áp đặt lên kinh nghiệm "
          "cảm tính. G.W.F. Hêghen đã trình bày các phạm trù trong sự vận động, chuyển hóa lẫn nhau, song "
          "coi đó là những nấc thang tự phát triển của “ý niệm tuyệt đối” [@bgd2021]. Chủ nghĩa duy vật "
          "biện chứng khắc phục cả quan niệm duy tâm chủ quan lẫn duy tâm khách quan: phạm trù là kết quả "
          "của quá trình nhận thức và thực tiễn, là sự phản ánh những mối liên hệ tồn tại khách quan vào "
          "trong ý thức con người. V.I. Lênin coi các phạm trù là những bậc thang của sự nhận thức thế "
          "giới, những điểm nút trong mạng lưới các hiện tượng tự nhiên, giúp con người nhận thức và làm "
          "chủ mạng lưới đó [@lenin29]."),
    ("h3", "1.1.2. Tính chất của phạm trù"),
    ("p", "Theo quan niệm duy vật biện chứng, phạm trù có những tính chất cơ bản sau [@bgd2021]. *Thứ "
          "nhất*, phạm trù có tính khách quan về nội dung, vì nội dung của nó là sự phản ánh những mối liên "
          "hệ tồn tại độc lập với ý thức; đồng thời có tính chủ quan về hình thức, vì nó là sản phẩm của "
          "tư duy trừu tượng. *Thứ hai*, phạm trù có tính phổ biến, vì những mặt, những mối liên hệ mà nó "
          "phản ánh có mặt trong mọi sự vật, hiện tượng. *Thứ ba*, phạm trù có tính biện chứng: các phạm "
          "trù liên hệ và chuyển hóa lẫn nhau, và nội dung của chúng không đứng im mà vận động theo sự "
          "vận động của hiện thực. *Thứ tư*, phạm trù có tính lịch sử: hệ thống phạm trù không khép kín mà "
          "được bổ sung, điều chỉnh cùng với sự phát triển của thực tiễn và của nhận thức khoa học."),
    ("p", "Các tính chất này có ý nghĩa trực tiếp đối với người nghiên cứu khoa học tự nhiên. Tính khách "
          "quan của phạm trù đòi hỏi các khái niệm khoa học phải được kiểm chứng trong đối tượng thực, chứ "
          "không được coi là những định nghĩa quy ước tùy tiện. Tính lịch sử của phạm trù cho thấy rằng "
          "ngay cả những khái niệm tưởng như ổn định của hóa học, như “acid”, “nguyên tố”, “hoạt tính ức "
          "chế”, cũng đã và đang thay đổi nội dung theo tiến trình của nhận thức, như sẽ được phân tích ở "
          "Chương 2."),
    ("h3", "1.1.3. Hệ thống các cặp phạm trù cơ bản và vị trí của cặp phạm trù bản chất – hiện tượng"),
    ("p", "Phép biện chứng duy vật khái quát sáu cặp phạm trù cơ bản: cái riêng và cái chung; nguyên nhân "
          "và kết quả; tất nhiên và ngẫu nhiên; nội dung và hình thức; bản chất và hiện tượng; khả năng và "
          "hiện thực. Các cặp phạm trù này cụ thể hóa hai nguyên lý cơ bản (nguyên lý về mối liên hệ phổ "
          "biến và nguyên lý về sự phát triển) và bổ sung cho ba quy luật cơ bản của phép biện chứng, song "
          "mỗi cặp phản ánh một phương diện riêng của các mối liên hệ [@bgd2021]. Cặp phạm trù bản chất và "
          "hiện tượng phản ánh quan hệ giữa mặt bên trong, tương đối ổn định, quy định sự vận động của sự "
          "vật với mặt bên ngoài, biến đổi, có thể quan sát trực tiếp. Do liên quan trực tiếp đến sự chuyển "
          "hóa từ nhận thức cảm tính lên nhận thức lý tính, cặp phạm trù này có ý nghĩa đặc biệt đối với lý "
          "luận nhận thức và đối với phương pháp luận của các khoa học thực nghiệm."),

    # ------------------------------------------------------------------ 1.2
    ("h2", "1.2. Lịch sử vấn đề bản chất và hiện tượng trong triết học"),
    ("p", "Quan hệ giữa bản chất và hiện tượng gắn liền với mặt thứ hai trong vấn đề cơ bản của triết học: "
          "con người có khả năng nhận thức được thế giới hay không. Những câu trả lời khác nhau cho câu hỏi "
          "này đã hình thành khả tri luận và bất khả tri luận, và qua đó hình thành những quan niệm khác "
          "nhau về bản chất và hiện tượng [@bgd2015; @bgd2021]."),
    ("h3", "1.2.1. Triết học Hy Lạp cổ đại"),
    ("p", "Ngay từ triết học Hy Lạp cổ đại, sự phân biệt giữa cái hiện ra trước giác quan và cái tồn tại "
          "thực sự đã được đặt ra. Đêmôcrít cho rằng các tính chất như ngọt, đắng, nóng, lạnh, màu sắc chỉ "
          "tồn tại theo “ước lệ”, còn trong thực tại chỉ có nguyên tử và khoảng trống; qua đó, ông đã phân "
          "biệt thế giới cảm tính với cấu trúc vật chất ẩn giấu ở bên dưới, dù ở trình độ trực quan, phỏng "
          "đoán. Platôn đi theo hướng duy tâm khách quan: bản chất chân thực là thế giới ý niệm, còn các sự "
          "vật cảm tính chỉ là cái bóng, bản sao không hoàn hảo của ý niệm. Arixtốt phê phán Platôn, khẳng "
          "định bản chất không tồn tại tách rời mà ở ngay trong các sự vật riêng lẻ, song quan niệm của ông "
          "còn dao động giữa chủ nghĩa duy vật và chủ nghĩa duy tâm [@bgd2015]."),
    ("h3", "1.2.2. Triết học Tây Âu cận đại và triết học cổ điển Đức"),
    ("p", "Trong triết học cận đại, J. Lốccơ phân biệt “chất có đầu tiên” (quảng tính, hình dạng, vận động) "
          "tồn tại trong bản thân vật thể với “chất có thứ hai” (màu sắc, mùi vị, âm thanh) chỉ tồn tại "
          "trong cảm giác của chủ thể. G. Béccơli đi đến chủ nghĩa duy tâm chủ quan khi cho rằng tồn tại "
          "có nghĩa là được tri giác. Đ. Hium cho rằng con người chỉ biết được các ấn tượng cảm tính của "
          "mình và không thể biết có gì tồn tại ở phía sau chúng [@bgd2015]. I. Cantơ thừa nhận sự tồn tại "
          "khách quan của “vật tự nó”, nhưng khẳng định con người chỉ nhận thức được “hiện tượng”, tức "
          "là vật như nó hiện ra đối với chủ thể thông qua các hình thức tiên nghiệm của cảm tính và giác "
          "tính; còn “vật tự nó” là không thể nhận thức. Như vậy, ở Cantơ, bản chất và hiện tượng bị tách "
          "rời bằng một ranh giới về nguyên tắc."),
    ("p", "G.W.F. Hêghen phê phán sự tách rời đó. Trong học thuyết về bản chất thuộc *Khoa học lôgíc*, ông "
          "khẳng định bản chất phải hiện ra, và hiện tượng không phải là cái gì ngoài bản chất mà chính là "
          "sự biểu hiện của bản chất. Đây là đóng góp biện chứng quan trọng, được V.I. Lênin đánh giá cao "
          "và kế thừa trong *Bút ký triết học* [@lenin29]. Tuy nhiên, Hêghen quy cả bản chất lẫn hiện tượng "
          "về các nấc thang vận động của “ý niệm tuyệt đối”, nên biện chứng của ông là biện chứng duy tâm "
          "[@bgd2015; @bgd2021]."),
    ("h3", "1.2.3. Quan niệm của C. Mác và Ph. Ăngghen"),
    ("p", "C. Mác và Ph. Ăngghen đã cải tạo phép biện chứng của Hêghen trên cơ sở duy vật, qua đó đặt vấn "
          "đề bản chất và hiện tượng trên một nền tảng mới: bản chất là những mối liên hệ tất nhiên của bản "
          "thân hiện thực vật chất, chứ không phải của ý niệm, và nhận thức bản chất là quá trình phản ánh "
          "những mối liên hệ đó dựa trên thực tiễn [@bgd2015; @bgd2021]. Trong *Tư bản*, Mác không chỉ nêu "
          "nguyên tắc này mà còn vận dụng nó như một phương pháp nghiên cứu. Ở chương cuối của quyển III, khi "
          "phân tích cái gọi là “công thức ba ngôi” (tư bản – lợi nhuận, ruộng đất – địa tô, lao động – tiền "
          "công), Mác phê phán kinh tế chính trị tầm thường vì nó chỉ hệ thống hóa những hình thái biểu hiện "
          "bề ngoài của các quan hệ kinh tế như chúng hiện ra trong ý thức của những người tham gia, mà không "
          "đi vào những mối liên hệ bên trong. Chính trong bối cảnh này, Mác nêu nhận định rằng nếu hình thái "
          "biểu hiện và bản chất của sự vật trực tiếp trùng khớp với nhau thì mọi khoa học đều trở nên thừa "
          "[@marx25]."),
    ("p", "Từ phân tích của Mác có thể rút ra hai điểm có ý nghĩa phương pháp luận chung. *Thứ nhất*, hình "
          "thái biểu hiện bề ngoài không phải là ảo ảnh chủ quan mà là cách thức khách quan mà các quan hệ bản "
          "chất hiện ra trong những điều kiện nhất định; vì thế, nó có thể được hệ thống hóa một cách chặt "
          "chẽ, và chính sự chặt chẽ ấy dễ khiến người ta lầm tưởng đã đạt tới bản chất. *Thứ hai*, khoa học "
          "chân chính không bác bỏ hình thái biểu hiện mà giải thích vì sao bản chất lại biểu hiện ra dưới "
          "hình thái ấy. Hai điểm này có giá trị vượt ra ngoài kinh tế chính trị: trong khoa học tự nhiên, một "
          "hệ thống số liệu được xử lý chặt chẽ về mặt thống kê vẫn có thể chỉ là sự hệ thống hóa hiện tượng, "
          "và nhiệm vụ của nhà nghiên cứu là giải thích vì sao hiện tượng lại xuất hiện như vậy."),
    ("h3", "1.2.4. Chủ nghĩa thực chứng, chủ nghĩa Makhơ và sự phê phán của V.I. Lênin"),
    ("p", "Từ thế kỷ XIX, chủ nghĩa thực chứng chủ trương khoa học chỉ cần mô tả các hiện tượng và những "
          "mối liên hệ đều đặn giữa chúng, không cần và không thể truy tìm bản chất. Chủ nghĩa kinh nghiệm "
          "phê phán của E. Makhơ và R. Avênariút đi xa hơn khi coi sự vật là “phức hợp những cảm giác”. "
          "Trong tác phẩm *Chủ nghĩa duy vật và chủ nghĩa kinh nghiệm phê phán*, V.I. Lênin đã phê phán "
          "các quan điểm này và khẳng định không có và không thể có sự khác nhau về nguyên tắc giữa hiện "
          "tượng và vật tự nó; chỉ có sự khác nhau giữa cái đã được nhận thức và cái chưa được nhận thức "
          "[@lenin18]. Để làm rõ luận điểm này, Lênin dẫn lại lập luận của Ph. Ăngghen về alizarin: chất "
          "màu trong rễ cây thiến thảo đã là “vật tự nó” chừng nào con người chưa biết đến cấu tạo của nó; "
          "khi hóa học hữu cơ tổng hợp được alizarin từ nhựa than đá, “vật tự nó” đã trở thành “vật cho ta” "
          "[@lenin18]. Như vậy, ranh giới giữa bản chất và hiện tượng không phải là ranh giới giữa cái có "
          "thể biết và cái không thể biết, mà là ranh giới lịch sử, có thể dịch chuyển, giữa cái đã biết và "
          "cái chưa biết; thực tiễn, trước hết là thực tiễn thí nghiệm và sản xuất, là phương tiện để dịch "
          "chuyển ranh giới đó."),
    ("p", "Lập luận về alizarin có ý nghĩa đặc biệt đối với người nghiên cứu hóa học. Nó cho thấy bản chất "
          "của một chất không phải là cái bí ẩn vĩnh viễn nằm sau các thuộc tính cảm tính, mà là cấu trúc "
          "và các mối liên hệ có thể được xác lập bằng phân tích, được kiểm chứng bằng tổng hợp và được sử "
          "dụng trong sản xuất. Khả năng tái tạo sự vật một cách có chủ đích là bằng chứng thực tiễn cao "
          "nhất cho tính đúng đắn của tri thức về bản chất của nó."),

    # ------------------------------------------------------------------ 1.3
    ("h2", "1.3. Quan niệm duy vật biện chứng về bản chất, hiện tượng và giả tượng"),
    ("h3", "1.3.1. Khái niệm bản chất và hiện tượng"),
    ("p", "Trên lập trường duy vật biện chứng, **bản chất** là tổng thể các mặt, các mối liên hệ tất nhiên, "
          "tương đối ổn định ở bên trong sự vật, quy định sự vận động và phát triển của sự vật đó; **hiện "
          "tượng** là sự biểu hiện ra bên ngoài của những mặt, những mối liên hệ ấy trong những điều kiện "
          "xác định [@bgd2021]. Cả bản chất và hiện tượng đều tồn tại khách quan, không phụ thuộc vào ý thức "
          "của con người. Hiện tượng không phải là cảm giác của chủ thể, mà là mặt của bản thân sự vật được "
          "đem lại cho con người trong cảm giác; bản chất không phải là một thực thể thứ hai đứng sau sự vật, "
          "mà là chính sự vật xét trong những mối liên hệ tất nhiên, bên trong của nó."),
    ("p", "Bản chất gắn liền với cái chung và cùng trình độ với quy luật: nói đến bản chất là nói đến cái "
          "tất nhiên, lặp lại trong những điều kiện nhất định. Tuy vậy, bản chất và quy luật không hoàn toàn "
          "đồng nhất. Quy luật là một mối liên hệ bản chất, tất nhiên, phổ biến và lặp lại giữa các mặt của "
          "sự vật; còn bản chất là tổng hợp nhiều mối liên hệ như vậy. Vì thế, bản chất là phạm trù rộng hơn "
          "và phong phú hơn quy luật [@bgd2015; @bgd2021]. Trong hóa học, định luật tuần hoàn là một quy "
          "luật; còn bản chất của nguyên tố hóa học là tổng thể các mối liên hệ giữa điện tích hạt nhân, cấu "
          "hình electron và các tính chất lý – hóa mà quy luật tuần hoàn chỉ biểu đạt một phương diện."),
    ("h3", "1.3.2. Giả tượng"),
    ("p", "Cần phân biệt hiện tượng với **giả tượng**. Giả tượng cũng là hiện tượng khách quan, nhưng biểu "
          "hiện bản chất dưới dạng xuyên tạc, khiến người quan sát, nếu dừng lại ở bề mặt, gán cho sự vật một "
          "bản chất mà nó không có [@bgd2015; @bgd2021]. Giả tượng khác với ảo giác chủ quan ở chỗ nó phát "
          "sinh từ chính các điều kiện khách quan trong đó bản chất được biểu hiện; do đó, không thể loại bỏ "
          "giả tượng bằng cách phủ nhận dữ kiện, mà chỉ có thể vượt qua nó bằng cách làm rõ những điều kiện "
          "đã sinh ra nó. Ví dụ quen thuộc là hiện tượng Mặt Trời “quay quanh” Trái Đất: đó là một biểu hiện "
          "có thật, được quan sát bởi mọi người, nhưng biểu hiện một bản chất ngược lại."),
    ("p", "Trong thực nghiệm khoa học, giả tượng thường xuất hiện khi điều kiện đo không được kiểm soát đầy "
          "đủ hoặc khi phương tiện đo tạo ra tín hiệu của chính nó. Như sẽ phân tích ở Chương 3, nhiều “hoạt "
          "tính” được ghi nhận trong thử nghiệm sinh học thuộc loại giả tượng: tín hiệu đo là có thật, nhưng "
          "nguyên nhân của nó không phải là cơ chế mà người nghiên cứu gán cho hợp chất."),
    ("h3", "1.3.3. Một minh họa hóa học"),
    ("p", "Quan hệ giữa bản chất và hiện tượng có thể được minh họa bằng tính acid của dung dịch. Tính acid "
          "biểu hiện ra qua giá trị pH đo được, màu của chất chỉ thị hay tốc độ phản ứng với kim loại; đó là "
          "những hiện tượng. Bản chất của tính acid là khả năng cho proton, được quy định bởi cấu trúc "
          "electron và độ bền của base liên hợp, thể hiện định lượng qua hằng số pK_{a}. Cùng một bản chất có "
          "thể biểu hiện thành những hiện tượng khác nhau tùy dung môi, nồng độ và nhiệt độ; ngược lại, cùng "
          "một hiện tượng (một giá trị pH) có thể xuất phát từ những bản chất khác nhau, chẳng hạn một acid "
          "mạnh ở nồng độ thấp và một acid yếu ở nồng độ cao. Minh họa này cho thấy không thể suy trực tiếp "
          "từ một hiện tượng riêng lẻ ra bản chất, mà phải xem xét hiện tượng trong hệ thống các điều kiện "
          "sinh ra nó."),

    # ------------------------------------------------------------------ 1.4
    ("h2", "1.4. Mối quan hệ biện chứng giữa bản chất và hiện tượng"),
    ("h3", "1.4.1. Sự thống nhất giữa bản chất và hiện tượng"),
    ("p", "Bản chất và hiện tượng thống nhất với nhau: bản chất bao giờ cũng bộc lộ ra thông qua hiện tượng, "
          "còn hiện tượng bao giờ cũng là sự biểu hiện của một bản chất nhất định. Không có bản chất thuần "
          "túy tồn tại tách rời hiện tượng, cũng không có hiện tượng hoàn toàn không biểu hiện bản chất. "
          "V.I. Lênin viết: “Bản chất hiện ra, hiện tượng là có tính bản chất” [@lenin29]. Sự thống nhất còn "
          "thể hiện ở chỗ bản chất và hiện tượng về căn bản phù hợp với nhau: bản chất nào thì hiện tượng "
          "ấy; khi bản chất thay đổi thì hiện tượng biểu hiện nó cũng thay đổi theo; khi bản chất mất đi thì "
          "hiện tượng tương ứng cũng mất đi [@bgd2021]. Chính sự thống nhất này là cơ sở khách quan cho khả "
          "năng nhận thức bản chất thông qua việc nghiên cứu hiện tượng, và là cơ sở để bác bỏ bất khả tri "
          "luận."),
    ("h3", "1.4.2. Sự đối lập giữa bản chất và hiện tượng"),
    ("p", "Sự thống nhất giữa bản chất và hiện tượng là sự thống nhất của các mặt đối lập. *Thứ nhất*, bản "
          "chất phản ánh cái chung, cái tất nhiên, quyết định sự tồn tại của sự vật, còn hiện tượng phản ánh "
          "cái riêng, cái cá biệt. Cùng một bản chất có thể biểu hiện ra thành nhiều hiện tượng khác nhau tùy "
          "theo điều kiện; chẳng hạn, sự chuyển electron trong phản ứng oxy hóa – khử có thể biểu hiện thành "
          "sự đổi màu của dung dịch, sự thoát khí, sự tỏa nhiệt hoặc dòng điện trong pin điện hóa. *Thứ hai*, "
          "bản chất là mặt bên trong, không thể nhận biết trực tiếp bằng giác quan; hiện tượng là mặt bên "
          "ngoài, có thể quan sát, đo đạc trực tiếp. *Thứ ba*, bản chất tương đối ổn định, còn hiện tượng "
          "thường xuyên biến đổi. Vì vậy, hiện tượng phong phú hơn bản chất, còn bản chất sâu sắc hơn hiện "
          "tượng [@bgd2015; @bgd2021]."),
    ("p", "Sự đối lập này không tuyệt đối. Tính “bên trong” của bản chất là tương đối với trình độ của "
          "phương tiện nhận thức: cấu trúc phân tử từng là cái ẩn giấu đối với hóa học thế kỷ XIX, nhưng ngày "
          "nay có thể được “quan sát” gián tiếp bằng phổ cộng hưởng từ hạt nhân hay nhiễu xạ tia X. Khi "
          "phương tiện nhận thức phát triển, một phần của bản chất trước đây chuyển thành cái có thể đo đạc, "
          "tức là trở thành hiện tượng ở một trình độ mới, và nhận thức lại tiếp tục đi sâu hơn."),
    ("h3", "1.4.3. Tính nhiều cấp độ của bản chất"),
    ("p", "Bản chất có nhiều cấp độ. V.I. Lênin chỉ ra rằng tư tưởng của con người không ngừng đi sâu từ "
          "hiện tượng đến bản chất, từ bản chất cấp một đến bản chất cấp hai và cứ thế tiếp tục [@lenin29]. "
          "Luận điểm này có ba hệ quả phương pháp luận. *Một là*, tri thức về bản chất ở mỗi cấp độ là tri "
          "thức tương đối, đúng trong những giới hạn xác định. *Hai là*, bản chất ở cấp độ sâu hơn không xóa "
          "bỏ mà bao hàm và giải thích bản chất ở cấp độ nông hơn, tức là quan hệ giữa các cấp độ bản chất "
          "tuân theo quy luật phủ định biện chứng, có kế thừa. *Ba là*, cái được coi là bản chất ở cấp độ này "
          "có thể lại là hiện tượng đối với cấp độ sâu hơn; chẳng hạn, định luật tuần hoàn là bản chất của sự "
          "lặp lại tính chất các nguyên tố, nhưng bản thân nó lại là biểu hiện của cấu trúc lớp vỏ electron."),

    # ------------------------------------------------------------------ 1.5
    ("h2", "1.5. Cặp phạm trù bản chất – hiện tượng trong hệ thống phép biện chứng duy vật"),
    ("h3", "1.5.1. Liên hệ với các cặp phạm trù khác"),
    ("p", "Các cặp phạm trù của phép biện chứng duy vật không tồn tại biệt lập mà liên hệ, bổ sung cho nhau. "
          "Xem xét cặp phạm trù bản chất – hiện tượng trong mối liên hệ với các cặp phạm trù khác giúp làm rõ "
          "hơn nội dung của nó và mở rộng khả năng vận dụng (Bảng 1.1)."),
    ("p", "Với cặp phạm trù *cái chung – cái riêng*, bản chất thuộc về cái chung, còn hiện tượng mang tính "
          "cá biệt. Một phép đo riêng lẻ là cái riêng; chỉ khi so sánh nhiều phép đo, nhiều sự vật cùng loại, "
          "cái chung, và qua đó bản chất, mới bộc lộ. Với cặp phạm trù *nguyên nhân – kết quả*, một hiện "
          "tượng có thể là kết quả của nhiều nguyên nhân khác nhau; nhận thức bản chất đòi hỏi xác định đúng "
          "nguyên nhân thực sự trong số các nguyên nhân có thể. Với cặp phạm trù *tất nhiên – ngẫu nhiên*, "
          "bản chất gắn với cái tất nhiên, còn hiện tượng chứa đựng cả những yếu tố ngẫu nhiên; cái tất "
          "nhiên chỉ được khẳng định khi nó được lặp lại qua nhiều điều kiện khác nhau."),
    ("p", "Với cặp phạm trù *nội dung – hình thức*, hình thức biểu hiện có thể không tương ứng với nội dung; "
          "việc căn cứ vào hình thức bên ngoài để kết luận về nội dung là một dạng đồng nhất hiện tượng với "
          "bản chất. Với cặp phạm trù *khả năng – hiện thực*, một hiện tượng quan sát được trong điều kiện "
          "hạn chế mới chỉ ra một khả năng; khả năng chỉ chuyển thành hiện thực khi hội đủ những điều kiện "
          "cần thiết. Trong nghiên cứu phát triển thuốc, một hợp chất có hoạt tính *in vitro* mới là khả năng "
          "của một thuốc, chưa phải hiện thực của nó."),
    ("table", "B1_1"),
    ("h3", "1.5.2. Liên hệ với các quy luật cơ bản của phép biện chứng"),
    ("p", "Cặp phạm trù bản chất – hiện tượng cũng liên hệ chặt chẽ với ba quy luật cơ bản của phép biện "
          "chứng duy vật. Với *quy luật chuyển hóa từ những thay đổi về lượng thành những thay đổi về chất và "
          "ngược lại*, bản chất của sự vật gắn liền với chất của nó: trong giới hạn của độ, những thay đổi về "
          "lượng chỉ biểu hiện ra thành những biến đổi của hiện tượng mà bản chất chưa thay đổi; khi vượt qua "
          "điểm nút, bản chất thay đổi và kéo theo sự thay đổi về chất của hiện tượng. Trong đánh giá hoạt "
          "tính, mối liên hệ này có một biểu hiện đáng chú ý: khi nồng độ của một chất có xu hướng kết tập "
          "vượt quá một ngưỡng nhất định, phân tử chuyển sang trạng thái keo và “hoạt tính ức chế” xuất hiện "
          "đột ngột, thường kèm theo đường cong liều – đáp ứng có độ dốc lớn bất thường [@shoichet2006; "
          "@feng2007]. Bước nhảy về chất ở đây thuộc về trạng thái hóa lý của hệ, không thuộc về tương tác "
          "giữa phân tử và enzyme; nhầm lẫn hai loại bước nhảy này là một nguồn gốc của giả tượng."),
    ("p", "Với *quy luật thống nhất và đấu tranh của các mặt đối lập*, bản thân quan hệ giữa bản chất và "
          "hiện tượng là một thể thống nhất của các mặt đối lập. Trong nhận thức, mâu thuẫn giữa tri thức đã "
          "có về bản chất và những hiện tượng mới không phù hợp với tri thức ấy là nguồn gốc và động lực của "
          "sự phát triển nhận thức; việc giải quyết mâu thuẫn đó dẫn đến tri thức về bản chất ở cấp độ sâu "
          "hơn. Với *quy luật phủ định của phủ định*, sự phát triển của nhận thức về bản chất diễn ra thông qua "
          "những lần phủ định biện chứng: tri thức mới phủ định tri thức cũ nhưng giữ lại những yếu tố hợp lý "
          "của nó, và sự phát triển có tính kế thừa, tính tiến lên. Các mối liên hệ này sẽ được minh họa qua "
          "lịch sử hóa học ở Chương 2."),

    # ------------------------------------------------------------------ 1.6
    ("h2", "1.6. Bản chất và hiện tượng trong tiến trình nhận thức"),
    ("h3", "1.6.1. Con đường biện chứng của sự nhận thức"),
    ("p", "Theo lý luận phản ánh của chủ nghĩa duy vật biện chứng, nhận thức là quá trình phản ánh tích cực, "
          "sáng tạo hiện thực khách quan vào bộ óc con người trên cơ sở thực tiễn. V.I. Lênin đã khái quát: "
          "“Từ trực quan sinh động đến tư duy trừu tượng, và từ tư duy trừu tượng đến thực tiễn – đó là con "
          "đường biện chứng của sự nhận thức chân lý, của sự nhận thức thực tại khách quan” [@lenin29]. Ở "
          "giai đoạn nhận thức cảm tính, thông qua cảm giác, tri giác và biểu tượng, con người tiếp nhận "
          "hiện tượng. Ở giai đoạn nhận thức lý tính, thông qua khái niệm, phán đoán và suy luận, con người "
          "trừu tượng hóa khỏi những yếu tố ngẫu nhiên, cá biệt để nắm bắt cái chung, cái tất nhiên, tức là "
          "bản chất [@bgd2021]."),
    ("p", "Hai giai đoạn này thống nhất với nhau. Nhận thức lý tính phải dựa trên tài liệu do nhận thức cảm "
          "tính cung cấp; tách khỏi hiện tượng, tư duy trừu tượng dễ rơi vào tư biện. Ngược lại, nhận thức "
          "cảm tính chỉ đem lại hiện tượng; dừng lại ở đó, nhận thức rơi vào chủ nghĩa kinh nghiệm hẹp hòi. "
          "Trong khoa học thực nghiệm hiện đại, nhận thức cảm tính được mở rộng bằng các thiết bị đo; do "
          "đó, “hiện tượng” mà nhà khoa học tiếp nhận không còn là cảm giác trực tiếp, mà là tín hiệu đã "
          "được thiết bị và các giả định lý thuyết trung gian. Điều này làm tăng khả năng tiếp cận bản chất, "
          "nhưng cũng làm xuất hiện những dạng giả tượng mới gắn với chính phương tiện đo."),
    ("p", "Điều này không làm mất đi tính khách quan của hiện tượng khoa học. Theo quan điểm duy vật biện "
          "chứng, phản ánh là một quá trình tích cực, được trung gian bởi hoạt động thực tiễn; thiết bị đo "
          "là sản phẩm của thực tiễn và là sự vật chất hóa của những tri thức đã được kiểm nghiệm. Kết quả đo "
          "vì vậy là một hiện tượng khách quan, nhưng là hiện tượng của một *quan hệ*: quan hệ giữa đối tượng "
          "nghiên cứu, phương tiện đo và điều kiện đo. Khi quên đi tính chất quan hệ đó và coi kết quả đo là "
          "thuộc tính riêng của đối tượng, người nghiên cứu dễ gán cho đối tượng những đặc điểm thực ra thuộc "
          "về phương tiện hoặc điều kiện đo. Đây là cơ sở nhận thức luận của nhiều dạng giả tượng sẽ được "
          "phân tích ở Chương 3."),
    ("h3", "1.6.2. Mô hình, giả thuyết và chân lý"),
    ("p", "Trên con đường từ hiện tượng đến bản chất, khoa học sử dụng mô hình và giả thuyết như những hình "
          "thức trung gian. Mô hình là sự tái hiện có đơn giản hóa đối tượng; nó phản ánh một số mặt của "
          "bản chất trong những giới hạn xác định. Giả thuyết là một phán đoán về bản chất chưa được chứng "
          "minh; nó chỉ trở thành lý thuyết khi được thực tiễn kiểm nghiệm. Nhầm lẫn mô hình với đối tượng, "
          "hoặc coi giả thuyết là chân lý đã được xác lập, là hai dạng sai lầm nhận thức luận phổ biến."),
    ("p", "Chân lý là tri thức phù hợp với hiện thực khách quan và được thực tiễn kiểm nghiệm. Chân lý có "
          "tính khách quan, tính tương đối và tính tuyệt đối, và tính cụ thể. Mọi tri thức về bản chất đạt "
          "được ở một thời điểm đều là chân lý tương đối, đúng trong những điều kiện xác định; tổng số các "
          "chân lý tương đối hợp thành chân lý tuyệt đối. Không có chân lý trừu tượng; chân lý luôn luôn là "
          "cụ thể, gắn với những điều kiện lịch sử – cụ thể của đối tượng được phản ánh [@bgd2021]."),
    ("h3", "1.6.3. Thực tiễn – tiêu chuẩn kiểm nghiệm tri thức về bản chất"),
    ("p", "Thực tiễn là cơ sở, động lực, mục đích và tiêu chuẩn của nhận thức. V.I. Lênin nhấn mạnh rằng "
          "quan điểm về đời sống, về thực tiễn phải là quan điểm thứ nhất và cơ bản của lý luận về nhận "
          "thức [@lenin18]. C. Mác, trong *Luận cương về Phoiơbắc*, khẳng định vấn đề tư duy của con người "
          "có thể đạt tới chân lý khách quan hay không là một vấn đề thực tiễn chứ không phải vấn đề lý luận "
          "thuần túy [@bgd2021]. Đối với khoa học thực nghiệm, thực tiễn bao gồm thí nghiệm có kiểm soát, "
          "sản xuất và ứng dụng. Một tri thức về bản chất chỉ được coi là đã kiểm chứng khi nó cho phép dự "
          "báo và tạo ra những hiện tượng mới trong những điều kiện mới, chứ không chỉ giải thích những "
          "hiện tượng đã có."),

    # ------------------------------------------------------------------ 1.7
    ("h2", "1.7. Ý nghĩa phương pháp luận"),
    ("p", "Từ những nội dung trên có thể rút ra bốn yêu cầu phương pháp luận, được sử dụng làm cơ sở cho "
          "việc phân tích ở các chương tiếp theo."),
    ("p", "*Thứ nhất*, nhận thức không được dừng lại ở hiện tượng mà phải đi đến bản chất. Chỉ khi nắm được "
          "bản chất, con người mới giải thích được đầy đủ các hiện tượng và tác động vào sự vật một cách có "
          "hiệu quả. Trong hoạt động thực tiễn, cần căn cứ vào bản chất chứ không căn cứ vào hiện tượng để "
          "đánh giá sự vật."),
    ("p", "*Thứ hai*, muốn nhận thức bản chất phải xuất phát từ hiện tượng, vì bản chất chỉ bộc lộ qua hiện "
          "tượng. Hơn nữa, cần nghiên cứu nhiều hiện tượng trong nhiều điều kiện khác nhau, vì một hiện "
          "tượng riêng lẻ chỉ phản ánh một phương diện của bản chất. Yêu cầu này là sự cụ thể hóa nguyên "
          "tắc khách quan và nguyên tắc toàn diện."),
    ("p", "*Thứ ba*, cần phân biệt hiện tượng điển hình với giả tượng. Lấy giả tượng làm căn cứ sẽ dẫn đến "
          "kết luận sai về bản chất và do đó dẫn đến hành động sai trong thực tiễn. Việc phân biệt này đòi "
          "hỏi làm rõ những điều kiện khách quan đã sinh ra hiện tượng."),
    ("p", "*Thứ tư*, nhận thức bản chất là quá trình đi từ bản chất cấp thấp đến bản chất cấp cao hơn, gắn "
          "với những điều kiện lịch sử – cụ thể; thực tiễn là tiêu chuẩn để kiểm nghiệm mức độ đúng đắn của "
          "tri thức về bản chất. Yêu cầu này là sự cụ thể hóa nguyên tắc lịch sử – cụ thể, nguyên tắc phát "
          "triển và nguyên tắc thống nhất giữa lý luận và thực tiễn."),
    ("p", "Vi phạm các yêu cầu trên dẫn đến hai khuynh hướng sai lầm đối lập nhau. Khuynh hướng thứ nhất là "
          "chủ nghĩa kinh nghiệm hẹp hòi: tuyệt đối hóa hiện tượng, coi dữ kiện quan sát được là bản chất, "
          "coi số liệu đo được là kết luận. Khuynh hướng thứ hai là chủ nghĩa giáo điều: xuất phát từ những "
          "khuôn mẫu, mô hình hoặc quy tắc có sẵn để phán xét sự vật mà không qua phân tích hiện tượng cụ "
          "thể. Cả hai khuynh hướng đều là biểu hiện của phương pháp tư duy siêu hình, tách rời bản chất "
          "khỏi hiện tượng."),

    ("sub", "Tiểu kết Chương 1"),
    ("p", "Chương 1 đã hệ thống hóa lịch sử vấn đề và quan niệm duy vật biện chứng về bản chất, hiện tượng "
          "và giả tượng. Bản chất và hiện tượng đều khách quan, thống nhất và đối lập với nhau; bản chất có "
          "nhiều cấp độ, và nhận thức bản chất là một quá trình vô tận, dựa trên thực tiễn. Ranh giới giữa "
          "bản chất và hiện tượng không phải là ranh giới giữa cái có thể biết và cái không thể biết, mà là "
          "ranh giới lịch sử giữa cái đã biết và cái chưa biết. Bốn yêu cầu phương pháp luận được rút ra ở "
          "mục 1.7 sẽ được sử dụng làm công cụ phân tích trong các chương tiếp theo."),
]
