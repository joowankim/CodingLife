import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const ChatRoomApp());
}


class ChatRoomApp extends StatelessWidget {
  const ChatRoomApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const CupertinoApp(
      home: ChatRoomList(),
    );
  }
}

class ChatRoomList extends StatelessWidget {
  const ChatRoomList({Key? key}) : super(key: key);

  Widget _appBar() {
    Widget _left() {
      return Expanded(
        child: Container(
          child: Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const Padding(
                padding: EdgeInsets.symmetric(horizontal: 8.0),
                child: Text('채팅',
                    style: TextStyle(
                        color: Colors.grey,
                        fontSize: 18,
                        fontWeight: FontWeight.bold)),
              ),
              Row(
                children: [
                  const Padding(
                    padding: EdgeInsets.symmetric(horizontal: 8.0),
                    child: Text('오픈채킹',
                        style: TextStyle(
                            fontSize: 18, fontWeight: FontWeight.bold)),
                  ),
                  Container(
                      width: 4,
                      height: 4,
                      decoration: const BoxDecoration(
                          shape: BoxShape.circle, color: Colors.redAccent))
                ],
              )
            ],
          ),
        ),
      );
    }

    Widget _right() {
      return Row(
        children: [
          IconButton(onPressed: () {}, icon: Icon(Icons.search)),
          IconButton(onPressed: () {}, icon: Icon(Icons.chat)),
          IconButton(onPressed: () {}, icon: Icon(Icons.music_note_rounded)),
          IconButton(onPressed: () {}, icon: Icon(Icons.settings)),
        ],
      );
    }

    return SafeArea(
      child: SizedBox(
        height: 60,
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [_left(), _right()],
        ),
      ),
    );
  }

  Widget _listItem() {
    Widget _left() {
      String image = '';
      return SizedBox(width: 60, height: 60, child: ClipRRect(borderRadius: BorderRadius.circular(8), child: Image.network(image)));
    }

    Widget _center() {
      String text = 'asdfzxvasf asdfzxcvasdf zxcvasdfqwerasdfzxcvsadfwqer';

      return Expanded(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                mainAxisAlignment: MainAxisAlignment.start,
                children: const [
                  Expanded(child: Text('IT 스택언더플로우 / aws 클라우드 가상화 개발', overflow: TextOverflow.ellipsis, style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold))),
                  SizedBox(width: 8),
                  Text('1160', style: TextStyle(color: Colors.grey, fontSize: 16)),
                  SizedBox(width: 8),
                  Icon(Icons.volume_off_outlined, color: Colors.grey, size: 14)
                ],
              ),
              const SizedBox(height: 8),
              Text(text, style: const TextStyle(color: Colors.grey, fontSize: 14), maxLines: 2, overflow: TextOverflow.ellipsis),
            ],
          ),
      );
    }

    Widget _right() {
      return Column(
        children: [
          const Text('오후 11:29'),
          const SizedBox(height: 8),
          Container(
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), color: Colors.red.shade300),
            child: const Padding(
              padding: EdgeInsets.symmetric(horizontal: 8.0, vertical: 4),
              child: Text('300+'),
            ),
          )
        ],
      );
    }

    return Row(
      children: [_left(), SizedBox(width: 16), _center(), SizedBox(width: 16), _right()],
    );
  }

  Widget _contents() {
    return Expanded(
        child: ListView.separated(
          itemBuilder: (BuildContext context, int index) => _listItem(),
          separatorBuilder: (BuildContext context, int index) => const Divider(height: 16),
          itemCount: 20,
          padding: const EdgeInsets.all(16),
        ),
    );
  }

  Widget _bottomNavigationBar() {
    return SizedBox(
      height: 60,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceAround,
        children: [
          IconButton(onPressed: () {}, icon: const Icon(Icons.person)),
          Stack(
            children: [
              IconButton(onPressed: () {}, icon: const Icon(Icons.chat)),
              Positioned(
                  top: 4,
                  right: 0,
                  child: Container(
                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), color: Colors.red.shade200),
                    child: const Padding(
                      padding: EdgeInsets.symmetric(vertical: 2.0, horizontal: 6.0),
                      child: Text(
                        '458',
                        style: TextStyle(fontSize: 12, color: Colors.white),
                      ),
                    ),
                  )
              ),
            ],
          ),
          IconButton(onPressed: () {}, icon: const Icon(Icons.remove_red_eye_outlined)),
          IconButton(onPressed: () {}, icon: const Icon(Icons.shopping_bag)),
          Stack(
            children: [
              IconButton(onPressed: () {}, icon: const Icon(Icons.menu)),
              Positioned(top: 4, right: 10, child: Container(width: 4, height: 4, decoration: const BoxDecoration(shape: BoxShape.circle, color: Colors.redAccent))),
            ],
          )
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [_appBar(), _contents(), _bottomNavigationBar()],
      )
    );
  }
}
